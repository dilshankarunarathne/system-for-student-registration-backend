import pymongo

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]
user_collection = mydb['attendance']





if __name__ == '__main__':
    print()
