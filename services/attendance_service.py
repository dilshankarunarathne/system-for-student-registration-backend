from dao.attendance_dao import query_attendance_info_for_student, query_attendance_info_for_class, delete_all_documents


def get_attendance_info_for_student(student_id):
    return query_attendance_info_for_student(student_id)


def get_attendance_info_for_lecture(course_id, date):
    return query_attendance_info_for_class(course_id, date)


def clear_all_records():
    return delete_all_documents()


def mark_attendance(student_id, course_id, date, attendance):
    attendance_info = query_attendance_info_for_student(student_id)
    if attendance_info is None:
        attendance_info = {
            'student_id': student_id,
            'attendance': []
        }
    attendance_info['attendance'].append({'course_id': course_id, 'date': date, 'attendance': attendance})
    return attendance_info
