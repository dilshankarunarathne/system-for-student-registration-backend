from fastapi import APIRouter

"""
    routers for attendance marking
"""

router = APIRouter(
    prefix="/api/attendance",
    tags=["attendance"],
    responses={404: {"description": "The requested page was not found"}},
)

@router.post("/facerec")
def 
