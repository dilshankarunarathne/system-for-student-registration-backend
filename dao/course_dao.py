import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
course_collection = mydb['course']


def query_all_courses():
    courses = list(course_collection.find())
    for course in courses:
        course['_id'] = str(course['_id'])
    if len(courses) == 0:
        return None
    return courses


def query_course_by_id(_id):
