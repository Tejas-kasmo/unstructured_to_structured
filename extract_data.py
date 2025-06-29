import pymongo as pm

def get_data():

    client = pm.MongoClient(r'mongodb://localhost:27017/')

    db = client["practice_data"]
    collection = db["project_2"]

    data = list(collection.find())

    return data

get_data('project')