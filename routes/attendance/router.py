from fastapi import APIRouter, UploadFile, File, Depends

"""
    routers for attendance marking
"""

router = APIRouter(
    prefix="/api/attendance",
    tags=["attendance"],
    responses={404: {"description": "The requested page was not found"}},
)

@router.post("/facerec")
def mark_by_face(
        image: UploadFile = File(...),
        token: str = Depends(oauth2_scheme)
)
    if image.content_type != "image/jpeg":
        return "Only jpeg images are supported"

    if get_current_user(token) is None:
        raise credentials_exception
