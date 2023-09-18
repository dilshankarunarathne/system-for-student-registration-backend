import mysql.connector
from mysql.connector import errorcode

"""
    middleware for accessing the student database and performing CRUD operations on the fingerprint table
"""


class FingerprintDAO:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def disconnect(self):
        if self.cnx is not None:
            self.cnx.close()

    def add_fingerprint(self, fingerprint_data):
        if fingerprint_data is None:
            raise ValueError("fingerprint data is null")

        cursor = self.cnx.cursor()
        add_fingerprint = ("INSERT INTO fingerprint "
                    "(id, username, email, is_instructor, hashed_password) "
                    "VALUES (%s, %s, %s, %s, %s)")
        data_user = (user.id, user.username, user.email, user.is_instructor, user.hashed_password)
        cursor.execute(add_user, data_user)
        self.cnx.commit()
        cursor.close()