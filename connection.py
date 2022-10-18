import pymongo

def connect():
    cliente = pymongo.MongoClient("localhost", 27017)

    db = cliente.test
    return db