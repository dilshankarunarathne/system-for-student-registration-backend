from fastapi import APIRouter, Depends, HTTPException, status, Form

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.student_service import all_student_info, student_info_by_id, student_info_by_uid

router = APIRouter(
    prefix="/api/student",
    tags=["student"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.get("/get-all")
async def get_all(
        token: str = Depends(oauth2_scheme)
):
    user = await get_current_user(token)

    if user is None:
        raise credentials_exception

    if user["role"] != "lecturer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only lecturers can access records",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return all_student_info()


@router.post("/get-by-id")
async def get_by_id(
        sid: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    user = await get_current_user(token)

    if user is None:
        raise credentials_exception

    return student_info_by_id(sid)


@router.get("/get-by-uid")
async def get_by_uid(
        uid: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    user = await get_current_user(token)

    if user is None:
        raise credentials_exception

    return student_info_by_uid(uid)
