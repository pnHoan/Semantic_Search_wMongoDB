from traceback import print_tb
import openai
import pymongo
import pandas as pd
import numpy as np
import APIkey
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity


openai.api_key = APIkey.get_key() 

# connect database
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["logTest"]
collection = db["logTest"]

def readData():
    df = pd.DataFrame(list(collection.find()))
    return df

def embedDatabase():
    df = readData()
    df['embedding'] = df['req'].apply(lambda x: get_embedding(x , engine='text-embedding-ada-002'))
    df.to_csv('embedded_database.csv')

# def semanticSearch(req_vec):
#     # tmp read data from csv
#     # df = pd.read_csv('embedded_database.csv')
#     df = pd.read_csv('database.csv')
#     df['embedding'] = df['embedding'].apply(eval).apply(np.array)

#     # Calculate similarity using cosine_similarity
#     df['similarities'] = df['embedding'].apply(lambda x: cosine_similarity(x, req_vec))
#     # TODO: [2] remove this later
#     # tmp print here
#     print(df[["req","similarities"]].sort_values("similarities", ascending=False))
#     # temp 
#     msg1 = df[["req","similarities"]].sort_values("similarities", ascending=False).values[0,0]
#     msg2 = df[["req","similarities"]].sort_values("similarities", ascending=False).values[1,0]

def semanticSearch(req_vec):
    df = pd.read_csv('database.csv')
    df['embedding'] = df['embedding'].apply(eval).apply(np.array)

    # Calculate similarity using cosine_similarity
    df['similarities'] = df['embedding'].apply(lambda x: cosine_similarity(x, req_vec))

    msg1 = df[["req","similarities"]].sort_values("similarities", ascending=False).values[0,0]
    msg2 = df[["req","similarities"]].sort_values("similarities", ascending=False).values[1,0]

    if 1: 
        print(df[["req","similarities"]].sort_values("similarities", ascending=False))
        print("======================================================================")

    return "The previous requests are: '{0}', '{1}' ".format(msg1, msg2) 

def newReqHandle(req):
    req_vec = get_embedding(req, engine="text-embedding-ada-002")
    return semanticSearch(req_vec)

if __name__ == "__main__":
    if 1:
        user_new_req = "what accessories do i need to buy for this ?"
        print(newReqHandle(user_new_req))

