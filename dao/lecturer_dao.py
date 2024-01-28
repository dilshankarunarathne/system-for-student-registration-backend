import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
lecturer_collection = mydb['lecturer']


def get_lecturer_info_by_uid(_u_id):
    filt = {'u_id': _u_id}
    lecturer = lecturer_collection.find_one(filt)
    return lecturer
