# models.py
"""
Basic data models for FoodWeb Login System (MongoDB)
"""
from datetime import datetime

class User:
    def __init__(self, username, password_hash, created_at=None, _id=None):
        self._id = _id
        self.username = username
        self.password_hash = password_hash
        self.created_at = created_at or datetime.utcnow()

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data.get('username'),
            password_hash=data.get('password_hash'),
            created_at=data.get('created_at'),
            _id=data.get('_id')
        )

    def to_dict(self):
        return {
            'username': self.username,
            'password_hash': self.password_hash,
            'created_at': self.created_at
        }
