from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str | None = None
    email: str | None = None
    role: str | None = None


class UserInDB(User):
    hashed_password: str
