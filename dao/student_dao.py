import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
user_collection = mydb['student']


def insert_student(_id, student_name, student_year, student_semester):
    student = {
        'id': _id,
        'name': student_name,
        'academic_year': student_year,
        'reg_no': reg_no,
        'u_id': _u_id
    }
    user_collection.insert_one(student)
    return student
