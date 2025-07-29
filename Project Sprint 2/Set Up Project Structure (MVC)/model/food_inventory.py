# food_inventory.py
"""
MongoDB Data Access for Food Inventory
"""
from pymongo import MongoClient, ASCENDING
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['foodweb_db']
foods = db['foods']

foods.create_index([('name', ASCENDING)], unique=True)

def add_food(name, category, price, quantity):
    food_doc = {
        'name': name,
        'category': category,
        'price': price,
        'quantity': quantity,
        'added_at': datetime.utcnow()
    }
    try:
        foods.insert_one(food_doc)
        return True
    except Exception:
        return False

def get_food(name):
    return foods.find_one({'name': name})

def update_quantity(name, quantity):
    result = foods.update_one({'name': name}, {'$set': {'quantity': quantity}})
    return result.modified_count > 0

def list_foods():
    return list(foods.find())
