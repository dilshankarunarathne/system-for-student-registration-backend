import pymongo
import gridfs
import base64

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["student"]

fs = gridfs.GridFS(mydb)


def get_all_students_info():
    studentinfo_collection = mydb['studentinfo']
    all_students = studentinfo_collection.find()
    for student in all_students:
        print(student)


def get_student_info_by_id(id):
    pass


def search_student_info_by_name(name):
    pass


def insert_student_info(student_info):
    pass


def store_student_capture(student_id, image):
    pass


if __name__ == '__main__':
    get_all_students_info()
