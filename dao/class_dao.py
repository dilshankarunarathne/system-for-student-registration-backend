import pymongo
from bson import json_util

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
class_collection = mydb['class']


def insert_class_info(class_info):
    result = class_collection.insert_one(class_info)
    return result.inserted_id
