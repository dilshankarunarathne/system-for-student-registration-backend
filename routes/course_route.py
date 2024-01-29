from fastapi import APIRouter

from services.course_service import get_all_courses

router = APIRouter(
    prefix="/api/course",
    tags=["course"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.get("/get-all")
async def get_all():
    data = get_all_courses()
    return {"operation": "successful", "data": data}
