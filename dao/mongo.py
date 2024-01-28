import pymongo
import gridfs
import base64

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["advertisement"]

fs = gridfs.GridFS(mydb)


def put_stat(stat: dict):
    mycol = mydb["stat"]
    stat.pop('_id', None)
    mycol.insert_one(stat)


def get_all_stats(month):
    mycol = mydb["stat"]
    filter = {"month": month}
    mydoc = mycol.find(filter).sort('_id', pymongo.DESCENDING)
    return mydoc[0]


def fetch_img_url(interest):
    mycol = mydb["ad"]

    filter = { "_id": 0, "interest": 1, "banner": 1 }
    myquery = {"interest": interest}

    mydoc = mycol.find(myquery, filter)

    return mydoc[0]["banner"]


def fetch_image(interest):
    interest = interest + ".jpg"
    file = fs.find_one({'filename': interest}, sort=[('uploadDate', -1)])
    if file:
        return file.read()
    else:
        return None


def fetch_all_images(gender):
    # fetch 5 random images and their filenames
    pipeline = [
        {'$match': {'gender': gender, 'age': {'$exists': True, '$ne': None}}},
        {'$sample': {'size': 5}}
    ]

    random_files = fs._GridFS__files.aggregate(pipeline)
    results = []

    for file in random_files:
        filename = file['filename']
        age = file['age']
        file_data = fs.get(file['_id']).read()

        # Convert the binary data to base64
        file_data_base64 = base64.b64encode(file_data).decode('utf-8')

        results.append((filename, file_data_base64, age))

    return results


def put_image_path(name, file_path):
    with open(file_path, 'rb') as f:
        image_id = fs.put(f, filename=name)
    return str(image_id)


def put_image(name, file, gender, age):
    image_id = fs.put(file, filename=name, gender=gender, age=age)
    return str(image_id)


def reformat_age(age):
    send_age = ""
    if age == "(0-2)":
        send_age = "4-14"
    elif age == "(4-6)":
        send_age = "4-14"
    elif age == "(8-12)":
        send_age = "4-14"
    elif age == "(15-20)":
        send_age = "13-26"
    elif age == "(25-32)":
        send_age = "27-40"
    elif age == "(38-43)":
        send_age = "27-40"
    elif age == "(48-53)":
        send_age = "Above 40"
    elif age == "(60-100)":
        send_age = "Above 40"

    return send_age


def fetch_ad_images(age_unformatted, gender):
    age = reformat_age(age_unformatted)

    pipeline = [
        {'$match': {'gender': gender, 'age': age}},
        {'$sample': {'size': 3}}
    ]

    random_files = fs._GridFS__files.aggregate(pipeline)

    results = []
    for file in random_files:
        filename = file['filename']
        file_data = fs.get(file['_id']).read()

        # Convert the binary data to base64
        file_data_base64 = base64.b64encode(file_data).decode('utf-8')

        results.append((filename, file_data_base64, age))

    return results
