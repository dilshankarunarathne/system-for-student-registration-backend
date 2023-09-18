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

    def

    def add_fingerprint(self, fingerprint_data, student_id: int):
        if fingerprint_data is None:
            raise ValueError("fingerprint data is null")

        cursor = self.cnx.cursor()
        add_fingerprint = ("INSERT INTO fingerprints "
                           "(id, student_id, fingerprint) "
                           "VALUES (%s, %s, %s)")
        data_fingerprint = (self.get_next_id(), student_id, fingerprint_data)
        cursor.execute(add_fingerprint, data_fingerprint)
        self.cnx.commit()
        cursor.close()

    def get_next_id(self) -> int:
        cursor = self.cnx.cursor()
        query = "SELECT MAX(id) FROM fingerprints"
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return 0
        return row[0]
