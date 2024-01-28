from fastapi import APIRouter, Form, Depends, HTTPException, status

from auth.authorize import credentials_exception, oauth2_scheme, get_current_user
from services.attendance_service import get_attendance_info_for_lecture, get_attendance_info_for_student

router = APIRouter(
    prefix="/api/attendance",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.post("/mark")


@router.post("/clear")
async def clear_all_records(
        token: str = Depends(oauth2_scheme)
):
    user = get_current_user(token)

    if user is None:
        raise credentials_exception

    if user["role"] != "lecturer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only lecturers can clear attendance records",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return clear_all_records()


@router.post("/get-student")
async def attendance_info_for_student(
        student_id: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if get_current_user(token) is None:
        raise credentials_exception

    return get_attendance_info_for_student(student_id)


@router.post("/get-lecture")
async def attendance_info_for_class(
        course_id: str = Form(...),
        date: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if get_current_user(token) is None:
        raise credentials_exception

    return get_attendance_info_for_lecture(course_id, date)
