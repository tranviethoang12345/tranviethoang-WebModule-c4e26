from db import food_collection, user_collection
from bson import ObjectId

def add_food(name, price):
    new_food = {
        "name": name,
        "price": price,
    }
    food_collection.insert_one(new_food)
    return new_food

def get_food(query): 
    food_list = food_collection.find(query)
    return food_list

def get_by_id_food(id):
    f = food_collection.find_one({ '_id': ObjectId(id) })
    return f

def delete_by_id_food(id):
    f = food_collection.delete_one({ '_id': ObjectId(id) })
    return f

def update_food(id, name, price):
    query = { '_id': ObjectId(id) }
    updater = { 
        "$set": { "name": name},
        "$set": { "price": price }, 
    } # $inc, $dec, $set, $unset
    f = food_collection.find_one_and_update(query, updater)
    return f

def find_by_username(username):
    f = user_collection.find_one(username["username"])
    return f

def add_user(username, password):
    new_user = {
        "username": username,
        "password": password,
    }
    user_collection.insert_one(new_user)
    return new_user