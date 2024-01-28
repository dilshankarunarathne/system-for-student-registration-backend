from fastapi import APIRouter, Form

from auth.authorize import credentials_exception
from services.attendance_service import get_attendance_info_for_lecture, get_attendance_info_for_student

router = APIRouter(
    prefix="/api/attendance",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.post("/student")
async def attendance_info_for_student(
        student_id: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if get_current_user(token) is None:
        raise credentials_exception

    return get_attendance_info_for_student(student_id)


@router.post("/lecture")
async def attendance_info_for_class(
        course_id: str = Form(...),
        date: str = Form(...),
):
    return get_attendance_info_for_lecture(course_id, date)
