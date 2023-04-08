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
        df = pd.DataFrame(list(self.collection.find()))
        df['embedding'] = df[field].apply(lambda x: get_embedding(x , engine='text-embedding-ada-002'))

        # tmp
        df.to_csv("tmp.csv")
        
        # Here
        for _,row in df.iterrows():
            # self.db.collection.update_one({'id': row.get('id')}, {'$set': row['embedding'].to_dict()}, upsert=False)
            self.db.collection.update_one({'id': row.get('id')}, {'$set': row.get('embedding')}, upsert=False)

            
            
        #TODO: add new fielf to mongodb Server
        

    def dropCollection(self):
        if self.db in self.client.list_database_names():
            db = self.client[self.db]
            if self.collection in db.list_collection_names():
                db[self.collection].drop()
                print(f"Collection {self.collection} dropped successfully from {self.db} database.")
            else:
                print(f"Collection {self.collection} does not exist in {self.db} database.")
        else:
            print(f"Database {self.db} does not exist.")
            
    def dropCollection(self, dbName,collectionName):
        if self.db in self.client.list_database_names():
            db = self.client[self.db]
            if self.collection in db.list_collection_names():
                db[self.collection].drop()
                print(f"Collection {self.collection} dropped successfully from {self.db} database.")
            else:
                print(f"Collection {self.collection} does not exist in {self.db} database.")
        else:
            print(f"Database {self.db} does not exist.")
