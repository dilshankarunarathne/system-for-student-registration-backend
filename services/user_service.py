from dao.user_dao import search_user_info_by_name, get_user_info_by_id, insert_user
from middleware.student_registration import register_student
from models.user_model import User


def add_new_user(username: str, password: str, email: str, role: str):
    # TODO: use middleware
    register_student()

    return insert_user(username, password, email, role)


def user_exists(username: str) -> bool:
    if get_user(username) is None:
        return False
    return True


def get_user(username: str):
    return search_user_info_by_name(username)


def get_user_by_id(user_id: int):
    return get_user_info_by_id(user_id)
