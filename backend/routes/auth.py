from fastapi import APIRouter, HTTPException
from backend.database import users_collection
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Hash password
def hash_password(password):
    return pwd_context.hash(password)


# Verify password
def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)


# Register
@router.post("/register")
def register(user: dict):

    existing = users_collection.find_one({"email": user["email"]})

    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user["password"] = hash_password(user["password"])

    result = users_collection.insert_one(user)

    return {"user_id": str(result.inserted_id)}


# Login
@router.post("/login")
def login(credentials: dict):

    user = users_collection.find_one({"email": credentials["email"]})

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(credentials["password"], user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode(
        {
            "user_id": str(user["_id"]),
            "exp": datetime.utcnow() + timedelta(hours=24)
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {"access_token": token}