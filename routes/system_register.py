from fastapi import APIRouter

"""
    routers for registering students inserting information to the db
"""

router = APIRouter(
    prefix="/api/register-student",
    tags=["attendance"],
    responses={404: {"description": "The requested page was not found"}},
)
