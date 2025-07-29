# login_dal.py
"""
Data Access Layer for Login System
Handles reading and writing user data to the database (users.json).
"""
import json
import os

DB_FILE = "users.json"

def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f)

def get_user(username):
    users = load_users()
    return users.get(username)

def add_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = password
    save_users(users)
    return True
