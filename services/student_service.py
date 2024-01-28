from dao.student_dao import get_all_students, query_student_info_by_id, query_student_info_by_uid


def all_student_info():
    students = get_all_students()
    return students


def student_info_by_id(_id):
    student = query_student_info_by_id(_id)
    return student


def student_info_by_uid(_u_id):
    student = query_student_info_by_uid(_u_id)
    return student
