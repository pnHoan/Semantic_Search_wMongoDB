import db_helper as sv
data = [
        {"id": 1, "type": "animals"},
        {"id": 2, "type": "foods"},
        {"id": 3, "type": "objects"},
        ]

if __name__ == "__main__":
    server = sv.Server(dbName="classifier",collectionName="classifierEmb")

    if server.checkExist():
        server.dropCollection(dbName="classifier",collectionName="classifierEmb")
    
    server.addData(data)
    
    if 1: #run once
        server.embeddingData("type")
    
    userInput = str(input("Enter object to classify: "))
    server.semanticSearch(userInput)
