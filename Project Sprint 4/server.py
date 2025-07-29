# server.py
"""
FastAPI server for Login System
Exposes endpoints for login and registration.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from login_bl import authenticate, register_user

app = FastAPI()

class UserCredentials(BaseModel):
    username: str
    password: str

class Donation(BaseModel):
    donor: str
    food_type: str
    amount: float
    location: str

class Pickup(BaseModel):
    volunteer: str
    pickup_location: str
    delivery_location: str
    food_type: str
    amount: float

# Example in-memory storage for donations and pickups
donations = []
pickups = []

@app.post("/login")
def login(creds: UserCredentials):
    success, message = authenticate(creds.username, creds.password)
    if success:
        return {"success": True, "message": message}
    else:
        raise HTTPException(status_code=401, detail=message)

@app.post("/register")
def register(creds: UserCredentials):
    success, message = register_user(creds.username, creds.password)
    if success:
        return {"success": True, "message": message}
    else:
        raise HTTPException(status_code=400, detail=message)

@app.post("/donate")
def donate(donation: Donation):
    donations.append(donation.dict())
    return {"success": True, "message": "Donation recorded.", "donation": donation.dict()}

@app.post("/pickup")
def pickup(pickup: Pickup):
    pickups.append(pickup.dict())
    return {"success": True, "message": "Pickup recorded.", "pickup": pickup.dict()}
