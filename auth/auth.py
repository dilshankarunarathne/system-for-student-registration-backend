from fastapi import APIRouter, Form, HTTPException, status

"""
    routers for authentication
"""

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post("/register")
async def register_user(
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        is_instructor: bool = Form(...),
):
    if user_exists(username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    hashed_password = get_password_hash(password)
    user = UserInDB(
        id=get_next_avail_id(),
        username=username,
        email=email,
        hashed_password=hashed_password,
        is_adviser=is_adviser,
    )
    add_new_user(user)
    return user