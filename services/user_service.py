from dao.lecturer_dao import insert_lecturer
from dao.student_dao import insert_student
from dao.user_dao import search_user_info_by_name, get_user_info_by_id, insert_user, get_role_by_id
from middleware.student_registration import register_student


def add_new_lecturer(username: str, password_hash: str, email: str, lecturer_name: str):
    user = _add_new_user(username, password_hash, email, 'student')
    _u_id = user['id']
    lecturer = insert_lecturer(lecturer_name, _u_id)

    if user and lecturer:
        return \
            {
                "message": "operation successful",
                "user_id": user['id'],
                "lecturer_id": lecturer['id'],
                "username": user['username']
            }


def add_new_student(username: str, password_hash: str, email: str, student_name: str, student_year: str, reg_no: str):
    # TODO: use middleware
    # register_student()

    user = _add_new_user(username, password_hash, email, 'student')
    _u_id = user['id']
    student = insert_student(student_name, student_year, reg_no, _u_id)

    if user and student:
        return \
            {
                "message": "operation successful",
                "user_id": user['id'],
                "student_id": student['id'],
                "username": user['username']
            }


def user_exists(username: str) -> bool:
    if get_user(username) is None:
        return False
    return True


def get_user(username: str):
    return search_user_info_by_name(username)


def get_user_by_id(user_id: int):
    return get_user_info_by_id(user_id)


def _add_new_user(username: str, password_hash: str, email: str, role: str):
    user = insert_user(username, password_hash, email, role)
    if user:
        return \
            {
                "message": "operation successful",
                "user": user['username'],
                "id": user['id']
            }
