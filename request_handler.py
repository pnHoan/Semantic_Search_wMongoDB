import pymongo
import openai
import pandas as pd
import numpy as np
import APIkey
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity



openai.api_key = APIkey.get_key()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["ReqTemplate"]

def CalEmbeding():
    # temp: export database into csv file
    df = pd.DataFrame(list(collection.find()))
    df['embedding'] = df['req'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
    df.to_csv('req_embeddings.csv')

def CalSimilarity(cus_req_vec):
    # TODO: Take data from database
    df = pd.read_csv('req_embeddings.csv')

    # Transform data from string to numpy array in order to calculate 
    df['embedding'] = df['embedding'].apply(eval).apply(np.array)

    df["similarities"] = df['embedding'].apply(lambda x: cosine_similarity(x, cus_req_vec))

    # temp: print and sort data here
    if 1:
        print(df[['req','similarities']].sort_values("similarities", ascending=False))
        print("=============================================")
    req = df[['req','similarities']].sort_values("similarities", ascending=False).values[0,0]
    print("the req is: {}".format(req))
    return None

def handleReq(cus_req):
    cus_req_vec = get_embedding(cus_req, engine="text-embedding-ada-002")
    CalSimilarity(cus_req_vec)

if __name__ == "__main__":
    if 0:
        CalEmbeding() # Embedding request data
    cus_req ="i want to talk to the manager"
    handleReq(cus_req)


