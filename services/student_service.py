def all_student_info():
    students = student_dao.get_all_students()
    return students