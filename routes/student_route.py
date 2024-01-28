from fastapi import APIRouter

router = APIRouter(
    prefix="/api/student",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.get("/get-all")
async def get_all(
        
):

