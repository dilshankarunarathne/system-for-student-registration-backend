from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer

"""
    authorization function middleware
"""

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://127.0.0.1:8000/auth/login")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user



