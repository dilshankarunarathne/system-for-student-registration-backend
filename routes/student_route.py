from fastapi import APIRouter

router = APIRouter(
    prefix="/api/student",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)



