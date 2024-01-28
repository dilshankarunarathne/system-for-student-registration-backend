import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
blacklist_collection = mydb['blacklist']


def blacklist_token(token):
    blacklist_collection.insert_one({'token': token})


def _get_next_id():
    last_user = blacklist_collection.find().sort('id', -1).limit(1)
    for user in last_user:
        return user['id'] + 1
