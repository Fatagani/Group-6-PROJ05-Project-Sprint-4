# transaction.py
"""
MongoDB Data Access for Transactions
"""
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['foodweb_db']
transactions = db['transactions']


def add_transaction(user_id, items, total):
    transaction_doc = {
        'user_id': user_id,
        'items': items,  # List of dicts: {food_id, quantity, price}
        'total': total,
        'timestamp': datetime.utcnow()
    }
    try:
        transactions.insert_one(transaction_doc)
        return True
    except Exception:
        return False

def get_transactions_by_user(user_id):
    return list(transactions.find({'user_id': user_id}))

def list_transactions():
    return list(transactions.find())
