import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
student_collection = mydb['student']


def get_all_students():
    students = list(student_collection.find())
    for student in students:
        student['_id'] = str(student['_id'])
    return students


def get_student_info_by_id(_id):
    filt = {'id': _id}
    student = student_collection.find_one(filt)
    return student


def get_student_info_by_uid(_u_id):
    filt = {'u_id': _u_id}
    student = student_collection.find_one(filt)
    return student


def insert_student(student_name, student_year, reg_no, _u_id):
    _id = _get_next_student_id()
    student = {
        'id': _id,
        'name': student_name,
        'academic_year': student_year,
        'reg_no': reg_no,
        'u_id': _u_id
    }
    student_collection.insert_one(student)
    return student


def _get_next_student_id():
    last_student = student_collection.find().sort('id', -1).limit(1)
    for student in last_student:
        return student['id'] + 1
