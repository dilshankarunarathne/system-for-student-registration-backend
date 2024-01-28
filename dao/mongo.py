import pymongo
import gridfs
import base64

client = pymongo.MongoClient("mongodb+srv://cluster-user:WSamCRFjm47IjoNT@cluster0.nwgoyl7.mongodb.net/")

mydb = client["studentinfo"]

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


def put_image(name, file, gender, age):
    image_id = fs.put(file, filename=name, gender=gender, age=age)
    return str(image_id)


def fetch_ad_images(age_unformatted, gender):
    age = age_unformatted

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


if __name__ == '__main__':
    print(mydb['text'])

