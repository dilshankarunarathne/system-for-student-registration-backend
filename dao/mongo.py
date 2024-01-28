import pymongo
import gridfs
import base64

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]

fs = gridfs.GridFS(mydb)

def get_all_students_info():
    pass


def get_student_info_by_id(id):
    pass


if __name__ == '__main__':
    pass
