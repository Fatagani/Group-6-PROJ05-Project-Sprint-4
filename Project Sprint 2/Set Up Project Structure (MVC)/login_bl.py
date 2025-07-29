
# login_bl.py
"""
Business Logic for Login System
Handles validation and authentication.
"""
from login_ui import get_user, add_user

def validate_username(username):
    # Example: username must be at least 3 chars, alphanumeric
    return username.isalnum() and len(username) >= 3

def validate_password(password):
    # Example: password must be at least 6 chars
    return len(password) >= 6

def authenticate(username, password):
    user_pw = get_user(username)
    if user_pw is not None and user_pw == password:
        return True, "Login successful! Welcome to FoodWeb."
    else:
        return False, "Invalid credentials."

def register_user(username, password):
    if not validate_username(username):
        return False, "Invalid username. Must be at least 3 alphanumeric characters."
    if not validate_password(password):
        return False, "Invalid password. Must be at least 6 characters."
    if add_user(username, password):
        return True, "Registration successful! Welcome to FoodWeb."
    else:
        return False, "Username already exists."
