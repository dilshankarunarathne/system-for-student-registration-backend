from dao.attendance_dao import query_attendance_info_for_student


def get_attendance_info_for_student(student_id):
    return query_attendance_info_for_student(student_id)


def get_attendance_info_for_class(course_id, date):
