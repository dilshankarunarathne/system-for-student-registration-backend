import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
user_collection = mydb['student']


def insert_student(student_name, student_year, reg_no, _u_id):
    _id = _get_next_student_id()
    student = {
        'id': _id,
        'name': student_name,
        'academic_year': student_year,
        'reg_no': reg_no,
        'u_id': _u_id
    }
    user_collection.insert_one(student)
    return student


def _get_next_student_id():
    last_student = user_collection.find().sort('id', -1).limit(1)
    for student in last_student:
        return student['id'] + 1
