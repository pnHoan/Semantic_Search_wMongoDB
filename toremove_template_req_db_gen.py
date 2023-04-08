import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["ReqTemplate"]


def printData():
    for doc in collection.find():
        print(doc) 

if __name__ == "__main__":
    if 1:
        collection.drop()
        data = [
            {"id": '1', "req": "buy product",               "action": "ask for which product"},
            {"id": '2', "req": "check receipt",             "action": "check bill id and send to customer"},
            {"id": '3', "req": "create bill",               "action": "generate bill"},
            {"id": '4', "req": "contact human assistant",   "action": "contact store owner"},
        ]

        _ = collection.insert_many(data)

    printData()
