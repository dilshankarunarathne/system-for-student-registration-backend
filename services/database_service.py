from dao.user_dao import UserDAO

dao = UserDAO(host="localhost", user="root", password="", database="enad")
try:
    dao.connect()
    print("EnAdDB connection successful")
except Exception as e:
    print("User DB connection error:", e)
