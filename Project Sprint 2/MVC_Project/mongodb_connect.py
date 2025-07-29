# MongoDB Connection Example for MVC Project

from pymongo import MongoClient

# Replace with your actual MongoDB URI
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "mvc_project"

# Create a MongoDB client and connect to the database
def get_db():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db

# Example usage:
if __name__ == "__main__":
    db = get_db()
    print("Collections:", db.list_collection_names())
    # Example: Insert a user
    user = {
        "username": "testuser",
        "password_hash": "hashed_pw",
        "email": "test@example.com",
        "role": "user"
    }
    db.users.insert_one(user)
    print("Inserted user:", user)
