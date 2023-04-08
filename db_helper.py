import pymongo
import pandas as pd
import numpy as np
import openai
import APIkey
from openai.embeddings_utils import get_embedding

openai.api_key = APIkey.get_key()

#default client (local host)
client = pymongo.MongoClient("mongodb://localhost:27017/")

class Server:
    def __init__(self,dbName, collectionName, clientName= "mongodb://localhost:27017/", ):
        self.client = pymongo.MongoClient(clientName)
        self.db = self.client[dbName]
        self.collection = self.db[collectionName]
    
    def addData(self,data: list):
        self.collection.insert_many(data)
    
    def printData(self):
        for item in self.collection.find():
            print(item)

    def embeddingData(self,field=""):
        '''Add embeded value of req'''
        collection = db[collectionName]
        
        df = pd.DataFrame(list(collection.find()))
        df['embedding'] = df[field].apply(lambda x: get_embedding(x , engine='text-embedding-ada-002'))

def dropCollection(dbName,collectionName):
    if dbName in client.list_database_names():
        db = client[dbName]
        if collectionName in db.list_collection_names():
            db[collectionName].drop()
            print(f"Collection {collectionName} dropped successfully from {dbName} database.")
        else:
            print(f"Collection {collectionName} does not exist in {dbName} database.")
    else:
        print(f"Database {dbName} does not exist.")
