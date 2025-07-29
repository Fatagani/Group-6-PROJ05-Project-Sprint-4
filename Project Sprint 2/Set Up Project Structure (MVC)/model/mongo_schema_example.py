# MongoDB User Schema Design (Python with PyMongo)
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

def add_user(username, password):
    user_doc = {
        'username': username,
        'password_hash': hash_password(password),
        'created_at': datetime.utcnow()
    }
    try:
        users.insert_one(user_doc)
        return True
    except Exception as e:
        return False

def get_user(username):
    return users.find_one({'username': username})

# Example usage:
# add_user('testuser', 'password123')
# user = get_user('testuser')
