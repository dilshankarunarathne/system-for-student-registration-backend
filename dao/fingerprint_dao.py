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
