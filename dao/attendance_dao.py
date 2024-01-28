import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
attendance_collection = mydb['attendance']


def query_attendance_info_for_student(student_id):
    filt = {'student_id': student_id}
    attendance = attendance_collection.find_one(filt)
    return attendance


def query_attendance_info_for_class(course_id, date):
    filt = {'course_id': course_id, 'date': date}
    attendance = attendance_collection.find_one(filt)
    return attendance


def delete_all_documents():
    result = attendance_collection.delete_many({})
    return result.deleted_count


def query_mark_attendance(attendance_info):
    result = attendance_collection.insert_one(attendance_info)
    return result.inserted_id
