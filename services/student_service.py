from dao.student_dao import get_all_students


def all_student_info():
    students = get_all_students()
    return students