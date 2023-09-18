from fastapi import APIRouter, UploadFile, File, Depends

from security.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.fingerprint_service import dao

"""
    routers for registering students inserting information to the db
"""

router = APIRouter(
    prefix="/api/register-student",
    tags=["attendance"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post
async def register_fingerprint(
        fingerprint_data: UploadFile = File(...),
        token: str = Depends(oauth2_scheme)
):
    if get_current_user(token) is None:
        raise credentials_exception

    dao.add_fingerprint()
