import pymongo
import pandas as pd
import numpy as np
import openai
import APIkey
from openai.embeddings_utils import get_embedding

openai.api_key = APIkey.get_key()
# connect db
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["Chatbot"]
collection = db["log"]

# TODO: add date time
logData = [
      {"id": "1", "userSessionId": "123", "req": "With 500$ which devices can i buy ?", "res": "you can buy ...."},
      {"id": "2", "userSessionId": "123", "req": "if i'm new to photography, should i pick <camera model> ?", "res": "To using this you should have some basic knowledge about photography like : ... <Lists of things to know>"},
      {"id": "3", "userSessionId": "123", "req": "what is ISO, exposure ,... <some others properties of photography>", "res": "Explaining some ideas..."},
      {"id": "4", "userSessionId": "123", "req": "I'd like to take some sceneries photos, which device should i take ?", "res": "Here are some model that suitable for request <list some devices>"},
]

# TODO: Remove this fn ?
# def readData():
#     '''Read data from database and return a Dataframe'''
#     df = pd.DataFrame(list(collection.find()))
#     return df

def embedDatabase():
    '''Add embeded value of req'''
    df = pd.DataFrame(list(collection.find()))
    df['embedding'] = df['req'].apply(lambda x: get_embedding(x , engine='text-embedding-ada-002'))

    # TODO: Remove the need of csv
    df.to_csv('database.csv')

def printColection():
    for item in collection.find():
        print(item)

def printCSV():
    df = pd.DataFrame(list(collection.find()))
    print(df['req'])

if __name__ == "__main__":
    if 0:
        collection.drop()
        _ = collection.insert_many(data)
        embedDatabase()
    printCSV()


# TODO: add new req
def AddNewReq():
    pass

