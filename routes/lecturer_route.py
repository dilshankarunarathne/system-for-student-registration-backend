from fastapi import APIRouter, Form

router = APIRouter(
    prefix="/api/lecturer",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.get("")
async def get_lecturer(
        lid: str = Form(...),
):
    return {"operation": "successful", "data": "lecturer"}
