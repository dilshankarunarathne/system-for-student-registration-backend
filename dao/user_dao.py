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
    filt = {'name': name}
    user = user_collection.find_one(filt)
    return user


def insert_user(username, email, password, role):
    user = {'username': username, 'email': email, 'role': role}
    user_collection.insert_one(user)


if __name__ == '__main__':
    pass
