from fastapi import APIRouter

router = APIRouter(
    prefix="/api/lecturer",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.get("")
async def get_lecturer(
        
):
    return {"operation": "successful", "data": "lecturer"}
