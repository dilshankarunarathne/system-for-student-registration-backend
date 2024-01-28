from pydantic import BaseModel


class Attendance(BaseModel):
    id: int
    username: str | None = None
    email: str | None = None
    role: str | None = None
