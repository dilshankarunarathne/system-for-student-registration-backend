from pydantic import BaseModel


class Attendance(BaseModel):
    id: int
    student_id: int
    course_id: int
    date: str
    attended_time: int
