import numpy as np

from fastapi import APIRouter, UploadFile, File, Depends
from starlette.responses import RedirectResponse

from security.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.fingerprint_service import add_fingerprint_to_db

"""
    routers for registering students inserting information to the db
"""

router = APIRouter(
    prefix="/api/register-student",
    tags=["attendance"],
    responses={404: {"description": "The requested page was not found"}},
)





@router.post
async def register_barcode(
        reg_no: str,
        barcode_data: UploadFile = File(...),
        token: str = Depends(oauth2_scheme)
):
    # TODO implement this
    pass


@router.post
async def register_fingerprint(
        reg_no: str,
        fingerprint_data: UploadFile = File(...),
        token: str = Depends(oauth2_scheme)
):
    """
    can register a fingerprint for a student, need to provide the student registration number along with it
    :param fingerprint_data: fingerprint data
    :param token: oauth2 token
    :param reg_no: student registration number
    :return: redirect to /user
    """
    if get_current_user(token) is None:
        raise credentials_exception

    contents = await fingerprint_data.read()
    nparray = np.fromstring(contents, np.uint8)

    add_fingerprint_to_db(nparray, reg_no)

    # TODO redirect user page
    return RedirectResponse("/user", status_code=200)
