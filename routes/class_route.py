from fastapi import APIRouter

router = APIRouter(
    prefix="/api/class",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)
