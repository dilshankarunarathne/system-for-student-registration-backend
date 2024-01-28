from config import config
from models.user_model import User


def add_new_user(user: User):
    pass


def user_exists(username: str) -> bool:
    pass


def get_next_avail_id() -> int:
    last_id = dao.get_last_user_id()
    if last_id is None:
        return 1
    return last_id + 1


def get_user(username: str):
    return dao.get_user_by_username(username)
