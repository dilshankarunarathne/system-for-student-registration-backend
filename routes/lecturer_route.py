from fastapi import APIRouter, Form

from services.lecturer_service import get_lecturer_by_id

router = APIRouter(
    prefix="/api/lecturer",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.get("")
async def get_lecturer(
        lid: str = Form(...),
):
    return get_lecturer_by_id(lid)
