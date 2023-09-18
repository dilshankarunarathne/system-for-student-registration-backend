from models.user_model import User

from dao.user_dao import UserDAO

dao = UserDAO(host="localhost", user="root", password="", database="enad")
try:
    dao.connect()
    print("EnAdDB connection successful")
except Exception as e:
    print("User DB connection error:", e)


def add_new_user(user: User):
    dao.create_user(user)


def user_exists(username: str) -> bool:
    if get_user(username) is None:
        return False
    return True


def get_next_avail_id() -> int:
    last_id = dao.get_last_user_id()
    if last_id is None:
        return 1
    return last_id + 1


def get_user(username: str):
    return dao.get_user_by_username(username)
