from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# 1,Connect
client = MongoClient(uri)

# 2,Get Datebase
db = client.c4e

# 3,Test
print("Connect Success")

# 4,Get collection
post_collection = db["posts"]
customers_collection = db["customers"]

# 4,Close connection
def close():
    client.close()  