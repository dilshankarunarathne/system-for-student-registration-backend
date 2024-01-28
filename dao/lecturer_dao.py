import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
lecturer_collection = mydb['lecturer']


def get_lecturer_info_by_uid(_u_id):
    filt = {'u_id': _u_id}
    lecturer = lecturer_collection.find_one(filt)
    return lecturer


def insert_lecturer(lecturer_name, _u_id):
    _id = _get_next_lecturer_id()
    lecturer = {
        'id': _id,
        'name': lecturer_name,
        'u_id': _u_id
    }
    lecturer_collection.insert_one(lecturer)
    return lecturer


def _get_next_lecturer_id():
    last_lecturer = lecturer_collection.find().sort('id', -1).limit(1)
    for lecturer in last_lecturer:
        return lecturer['id'] + 1
