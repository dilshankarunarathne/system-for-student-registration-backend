from dao.user_dao import search_user_info_by_name, get_user_info_by_id
from models.user_model import User


def add_new_user(user: User):
    # TODO: use middleware
    # TODO: add user to database
    pass


def user_exists(username: str) -> bool:
    if get_user(username) is None:
        return False
    return True


def get_user(username: str):
    return search_user_info_by_name(username)


def get_user_by_id(user_id: int):
    return get_user_info_by_id(user_id)
