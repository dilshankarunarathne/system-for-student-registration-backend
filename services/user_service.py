from config import config
from models.user_model import User


def add_new_user(user: User):
    # TODO: get files
    # TODO: store files
    pass


def user_exists(username: str) -> bool:
    if get_user(username) is None:
        return False
    return True


def get_user(username: str):
    pass
