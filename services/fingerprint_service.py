from dao.fingerprint_dao import FingerprintDAO
"""
    middleware services for fingerprint data
"""

dao = FingerprintDAO(host="localhost", user="root", password="", database="enad")
try:
    dao.connect()
    print("EnAdDB connection successful")
except Exception as e:
    print("User DB connection error:", e)


def add_fingerprint_to_db(fingerprint_data):
    # TODO add fingerprint data to the database
    pass


def check_fingerprint(fingerprint_data):
    # TODO check if a given fingerprint matches an existing user in the database
    pass


def check_against_all(fingerprint_data):
    fingerprints =
