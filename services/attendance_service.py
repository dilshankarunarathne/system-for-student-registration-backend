from dao.attendance_dao import query_attendance_info_for_student, query_attendance_info_for_class, delete_all_documents, \
    query_mark_attendance


def get_attendance_info_for_student(student_id):
    return query_attendance_info_for_student(student_id)


def get_attendance_info_for_lecture(course_id, date):
    return query_attendance_info_for_class(course_id, date)


def clear_all_records():
    return delete_all_documents()


def mark_attendance(student_id, course_id, date, attended_time, total_time):
    attendance_info = get_attendance_info_for_lecture(course_id, date)
    _id = _get_last_id()
    if attendance_info is None:
        attendance_info = {
            'id': None,
            'course_id': course_id,
            'date': date,
            "student_id": student_id,
            "attended_time": attended_time,
            "total_time": total_time
        }
    else:
        raise Exception("Attendance already marked for this lecture")
    return query_mark_attendance(attendance_info)



