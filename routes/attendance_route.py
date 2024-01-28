from datetime import datetime

from fastapi import APIRouter, Form, Depends, HTTPException, status

from auth.authorize import credentials_exception, oauth2_scheme, get_current_user
from middleware.attendance_calculator import get_percentage
from services.attendance_service import get_attendance_info_for_lecture, get_attendance_info_for_student, \
    mark_attendance, clear_all_records, create_placeholder_document

router = APIRouter(
    prefix="/api/attendance",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.post("/mark")
async def mark_single_attendance(
        course_id: str = Form(...),
        student_id: str = Form(...),
        attended_time: str = Form(...),
        total_time: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    user = await get_current_user(token)

    if user is None:
        raise credentials_exception

    date = datetime.now().strftime("%d/%m/%Y")

    doc_id, _id = mark_attendance(student_id, course_id, date, attended_time, total_time)

    return {"message": "operation successful", "attendance marked": _id}


@router.post("/clear")
async def clear_all(
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

    cur = clear_all_records()

    create_placeholder_document()

    return {"message": "operation successful", "attendance cleared": cur}


@router.post("/get-student")
async def attendance_info_for_student(
        student_id: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if await get_current_user(token) is None:
        raise credentials_exception

    attendance = get_attendance_info_for_student(student_id)

    (final_percentage, ext, ext_type) = get_percentage(attendance)

    return {"attendance": attendance, "percentage": final_percentage, "ext": ext, "ext_type": ext_type}


@router.post("/get-lecture")
async def attendance_info_for_class(
        course_id: str = Form(...),
        date: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if await get_current_user(token) is None:
        raise credentials_exception

    try:
        data = get_attendance_info_for_lecture(course_id, date)
    except TypeError:
        data = {"message": "No data found"}
    return data
