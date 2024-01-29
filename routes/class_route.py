from fastapi import APIRouter, Form

router = APIRouter(
    prefix="/api/class",
    tags=["class"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.put("")
def create_class(
        class_id: str = Form(...),
        class_name: str = Form(...),
        course_id: str = Form(...),
        student_ids: list = Form(...),
):
    pass


@router.get("")
def get_class_by_id(
        class_id: str = Form(...),
):
    pass
