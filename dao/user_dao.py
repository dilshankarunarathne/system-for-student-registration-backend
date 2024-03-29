import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
user_collection = mydb['user']


def get_all_users_info():
    lis = []
    all_users = user_collection.find()
    for user in all_users:
        lis.append(user)
    return lis


def get_user_info_by_id(u_id):
    filt = {'id': u_id}
    user = user_collection.find_one(filt)
    return user


def search_user_info_by_name(name):
    filt = {'username': name}
    user = user_collection.find_one(filt)
    return user


def insert_user(username, password_hash, email, role):
    user = {
        'id': _get_last_user_id() + 1,
        'username': username,
        'email': email,
        'hashed_password': password_hash,
        'role': role
    }
    user_collection.insert_one(user)
    return user


def get_role_by_id(user_id):
    filt = {'id': user_id}
    user = user_collection.find_one(filt)
    return user['role']


def _get_last_user_id():
    last_user = user_collection.find().sort('id', -1).limit(1)
    for user in last_user:
        return user['id']
