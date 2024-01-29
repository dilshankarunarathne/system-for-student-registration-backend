import pymongo
from bson import json_util

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
class_collection = mydb['class']


def query_class_info(course_id):
    filt = {'course_id': course_id}
    class_info = class_collection.find_one(filt)
    if not class_info:
        return None
    class_info['_id'] = str(class_info['_id'])
    return class_info


def insert_class_info(course_id, date, start_time, duration):
    _id = _get_next_id()
    class_collection.insert_one(
        {"id": _id, "course_id": course_id, "date": date, "start_time": start_time,
         "duration": duration}
    )
    return _id


def _get_next_id():
    return class_collection.count_documents({}) + 1
