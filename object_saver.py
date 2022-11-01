import os
import pymongo

client = pymongo.MongoClient(os.getenv('MONGO_URL'))
database = client[os.getenv('MONGO_DB')]
collection = database[os.getenv('MONGO_COLLECTION')]

def _save_object_to_mongo(data: dict) -> str:
    insert_result = collection.insert_one(data)
    return str(insert_result.inserted_id)

def save_object(data: dict) -> str:
    return _save_object_to_mongo(data)