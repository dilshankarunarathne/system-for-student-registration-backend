from models.user_model import User
from services.database_service import dao


def add_new_user(user: User):
    dao.create_user(user)


def user_exists(username: str) -> bool:
    if get_user(username) is None:
        return False
    return True
