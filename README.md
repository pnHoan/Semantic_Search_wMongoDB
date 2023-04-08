# Apply chatGPT into Facebook chatbot

# 
database = "Chatbot"
colection:
  - "shop"
  - "log"
  - "templateReq"

```
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["Chatbot"]
collection = db["log"]
```
