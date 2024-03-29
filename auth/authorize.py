from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

import config
from dao.token_dao import is_token_blacklisted
from models.token_model import TokenData
from auth.hashing import verify_password, SECRET_KEY, ALGORITHM
from services.user_service import get_user

tokenUrl = config.get("auth", "auth.tokenurl")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=tokenUrl)

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user['hashed_password']):
        return False
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    if is_token_blacklisted(token):
        raise credentials_exception
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
