from dao.student_dao import get_all_students


def all_student_info():
    students = get_all_students()
    print(students)
    return students


def get_student_info_by_id(_id):
    student = get_student_info_by_id(_id)
    return student
