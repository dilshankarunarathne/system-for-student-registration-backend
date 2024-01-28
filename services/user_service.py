from dao.user_dao import search_user_info_by_name, get_user_info_by_id, insert_user, get_role_by_id
from middleware.student_registration import register_student


def _add_new_user(username: str, password_hash: str, email: str, role: str):
    user = insert_user(username, password_hash, email, role)
    if user:
        return \
            {
                "message": "operation successful",
                "user": user['username'],
                "id": user['id']
            }


def add_new_student():
    # TODO: use middleware
    # register_student()

    pass


def user_exists(username: str) -> bool:
    if get_user(username) is None:
        return False
    return True


def get_user(username: str):
    return search_user_info_by_name(username)


def get_user_by_id(user_id: int):
    return get_user_info_by_id(user_id)
