 # models.py
 # Basic MongoDB models for MVC Project

from bson import ObjectId
class User:
    def __init__(self, username, password_hash, email, role="user", _id=None):
        self._id = _id or ObjectId()
        self.username = username
        self.password_hash = password_hash
        self.email = email
        self.role = role

    def to_dict(self):
        return {
            "_id": self._id,
            "username": self.username,
            "password_hash": self.password_hash,
            "email": self.email,
            "role": self.role
        }

class FoodItem:
    def __init__(self, name, category, nutrients, created_by, _id=None):
        self._id = _id or ObjectId()
        self.name = name
        self.category = category
        self.nutrients = nutrients  # dict: {calories, protein, fat, carbs}
        self.created_by = created_by

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "category": self.category,
            "nutrients": self.nutrients,
            "created_by": self.created_by
        }

class Category:
    def __init__(self, name, description, _id=None):
        self._id = _id or ObjectId()
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "description": self.description
        }

class Report:
    def __init__(self, user_id, food_item_id, report_type, data, created_at, _id=None):
        self._id = _id or ObjectId()
        self.user_id = user_id
        self.food_item_id = food_item_id
        self.report_type = report_type
        self.data = data
        self.created_at = created_at

    def to_dict(self):
        return {
            "_id": self._id,
            "user_id": self.user_id,
            "food_item_id": self.food_item_id,
            "report_type": self.report_type,
            "data": self.data,
            "created_at": self.created_at
        }


# Example usage for testing
if __name__ == "__main__":
    # Create a user
    user = User(username="alice", password_hash="hash123", email="alice@example.com", role="admin")
    print("User:", user.to_dict())

    # Create a category
    category = Category(name="Fruit", description="Edible sweet plant product")
    print("Category:", category.to_dict())

    # Create a food item
    nutrients = {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14}
    food_item = FoodItem(name="Apple", category="Fruit", nutrients=nutrients, created_by=user._id)
    print("FoodItem:", food_item.to_dict())

    # Create a report
    report_data = {"summary": "Good nutritional value."}
    from datetime import datetime
    report = Report(user_id=user._id, food_item_id=food_item._id, report_type="nutrition", data=report_data, created_at=datetime.utcnow())
    print("Report:", report.to_dict())
