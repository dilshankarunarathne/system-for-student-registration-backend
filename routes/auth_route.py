from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from auth.authorize import authenticate_user, oauth2_scheme, get_current_user, credentials_exception
from auth.hashing import get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from dao.token_dao import blacklist_token
from services.user_service import user_exists, add_new_student

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.post("/register-student")
async def register_student(
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        student_name: str = Form(...),
        student_year: str = Form(...),
        reg_no: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    user = await get_current_user(token)

    if user is None:
        raise credentials_exception

    if user["role"] != "lecturer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only lecturers can clear attendance records",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if user_exists(username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    hashed_password = get_password_hash(password)

    return add_new_student(username, hashed_password, email, student_name, student_year, reg_no)


@router.post("/register-lecturer")
async def register_lecturer(
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
):
    if user_exists(username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    hashed_password = get_password_hash(password)

    return add_new_user(username, hashed_password, email, role)



@router.post("/login")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['username']}, expires_delta=access_token_expires.seconds
        # Unresolved attribute reference 'username' for class 'bool'
    )

    return {"message": "operation successful", "access token": access_token, "token type": "bearer"}


@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    blacklist_token(token)
    return {"message": "Successfully logged out"}
