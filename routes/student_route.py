from fastapi import APIRouter, Depends, HTTPException, status

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception

router = APIRouter(
    prefix="/api/student",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.get("/get-all")
async def get_all(
        token: str = Depends(oauth2_scheme)
):
    user = await get_current_user(token)

    if user is None:
        raise credentials_exception

    if user["role"] != "lecturer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only lecturers can clear attendance records",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return all_student_info()
