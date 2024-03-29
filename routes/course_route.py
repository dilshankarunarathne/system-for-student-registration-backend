from fastapi import APIRouter, Depends, Form

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.course_service import get_all_courses, get_course_by_id

router = APIRouter(
    prefix="/api/course",
    tags=["course"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.post("/get-by-id")
async def get_by_id(
    cid: str = Form(...),
    token: str = Depends(oauth2_scheme)
):
    user = await get_current_user(token)

    if user is None:
        raise credentials_exception

    data = get_course_by_id(cid)
    return {"operation": "successful", "data": data}


@router.post("/get-all")
async def get_all(
    # token: str = Depends(oauth2_scheme)
):
    # user = await get_current_user(token)

    # if user is None:
    #     raise credentials_exception

    data = get_all_courses()
    return {"operation": "successful", "data": data}
