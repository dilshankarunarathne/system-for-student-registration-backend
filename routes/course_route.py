from fastapi import APIRouter

router = APIRouter(
    prefix="/api/course",
    tags=["course"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.get("/get-all")
async def get_all():
    return {"operation": "successful", "data": "all courses"}
