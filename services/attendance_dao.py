import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
user_collection = mydb['attendance']


def get_attendance_info_for_student(student_id):
    filt = {'student_id': student_id}
    attendance = user_collection.find_one(filt)
    return attendance





if __name__ == '__main__':
    print()
