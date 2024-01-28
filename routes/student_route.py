from fastapi import APIRouter, Depends

from auth.authorize import oauth2_scheme

router = APIRouter(
    prefix="/api/student",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.get("/get-all")
async def get_all(
        token: str = Depends(oauth2_scheme)
):

