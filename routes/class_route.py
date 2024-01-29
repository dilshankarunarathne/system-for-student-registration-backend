from fastapi import APIRouter, Form

from services.class_service import add_new_class

router = APIRouter(
    prefix="/api/class",
    tags=["class"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.put("")
def create_class(
        course_id: int = Form(...),
        date: str = Form(...),
        start_time: str = Form(...),
        duration: str = Form(...),
):
    data = add_new_class(course_id, date, start_time, duration)


@router.get("")
def get_class_by_id(
        class_id: str = Form(...),
):
    pass
