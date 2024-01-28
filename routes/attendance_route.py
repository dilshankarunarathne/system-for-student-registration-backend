from fastapi import APIRouter, Form

router = APIRouter(
    prefix="/api/attendance",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.post("/student")
async def get_attendance_info_for_student(
        student_id: str = Form(...),
):
    pass


@router.post("/lecture")
async def get_attendance_info_for_class(
        course_id: str = Form(...),
        date: str = Form(...),
):
    pass
