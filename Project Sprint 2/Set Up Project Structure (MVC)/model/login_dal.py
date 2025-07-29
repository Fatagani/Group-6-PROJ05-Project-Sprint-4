

# login_dal.py
"""
Data Access Layer for Login System (MongoDB)
Handles reading and writing user data to MongoDB.
"""
from pymongo import MongoClient, ASCENDING
from datetime import datetime
import hashlib

client = MongoClient('mongodb://localhost:27017/')
db = client['foodweb_db']
users = db['users']

# Ensure unique index on username
users.create_index([('username', ASCENDING)], unique=True)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_user(username):
    """
    Returns user document if found, else None.
    """
    return users.find_one({'username': username})

def add_user(username, password):
    """
    Adds a new user with hashed password. Returns True if successful, False if username exists or error.
    """
    if get_user(username):
        return False
    user_doc = {
        'username': username,
        'password_hash': hash_password(password),
        'created_at': datetime.utcnow()
    }
    try:
        users.insert_one(user_doc)
        return True
    except Exception:
        return False
