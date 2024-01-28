import pymongo
import gridfs
import base64

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
studentinfo_collection = mydb['user']


def get_all_users_info():
    lis = []
    all_users = studentinfo_collection.find()
    for user in all_users:
        lis.append(user)
    return lis


def get_user_info_by_id(s_id):
    filt = {'id': s_id}
    user = studentinfo_collection.find_one(filt)
    return user


def search_user_info_by_name(name):
    filt = {'name': name}
    user = studentinfo_collection.find_one(filt)
    return user


def insert_user(name, email, password, role):
    user = {'name': name, 'email': email, 'password': password, 'role': role}
    studentinfo_collection.insert_one(user)


if __name__ == '__main__':
    pass
