from fastapi import APIRouter, Form, Depends, HTTPException, status

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.class_service import add_new_class, get_class_info

router = APIRouter(
    prefix="/api/class",
    tags=["class"],
    responses={404: {"description": "The requested url was not found"}},
)


# TODO get last class info
# TODO edit course info


@router.put("")
async def create_class(
        course_id: int = Form(...),
        date: str = Form(...),
        start_time: str = Form(...),
        duration: str = Form(...),
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

    data = add_new_class(course_id, date, start_time, duration)
    return {"message": "operation successful"}


@router.get("")
async def get_class_by_id(
        class_id: int = Form(...),
        token: str = Depends(oauth2_scheme)
):
    user = await get_current_user(token)

    if user is None:
        raise credentials_exception

    return get_class_info(class_id)
