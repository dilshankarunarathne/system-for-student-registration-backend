

"""
    routers for attendance marking
"""
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/attendance",
    tags=["attendance"],
    responses={404: {"description": "The requested page was not found"}},
)
