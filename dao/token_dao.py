from datetime import datetime

import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
blacklist_collection = mydb['blacklist']


def blacklist_token(token):
    _id = _get_next_id()
    current_time = datetime.now()

    blacklist_collection.insert_one(
        {
            'id': _id,
            'token': token,
            'timestamp': current_time
        }
    )


def is_token_blacklisted(token):
    filt = {'token': token}
    user = blacklist_collection.find_one(filt)
    return user is not None


def _get_next_id():
    last_user = blacklist_collection.find().sort('id', -1).limit(1)
    for user in last_user:
        return user['id'] + 1
