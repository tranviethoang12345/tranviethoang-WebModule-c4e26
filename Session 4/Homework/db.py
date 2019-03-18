from pymongo import MongoClient

uri = "mongodb+srv://admin:admin1@max-oaxts.mongodb.net/test?retryWrites=true"

# 1,Connect 
client = MongoClient(uri)

# 2,Get Datebase
db = client.test

# 3,Get collection
food_collection = db["food"] # collection
user_collection=db["users"] 

# 4,Close connection
def close():
    client.close()  