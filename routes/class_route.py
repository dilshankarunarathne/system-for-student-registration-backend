from fastapi import APIRouter, Form

from services.class_service import add_new_class

router = APIRouter(
    prefix="/api/class",
    tags=["class"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.put("")
def create_class(
        class_id: str = Form(...),
        course_id: str = Form(...),
        student_ids: list = Form(...),
):
    return add_new_class(class_id, course_id, student_ids)


@router.get("")
def get_class_by_id(
        class_id: str = Form(...),
):
    pass
