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





if __name__ == '__main__':
    pass
