from pymongo import MongoClient
import os

MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)

db = client["ecommerce"]

users_collection = db["users"]
products_collection = db["products"]
orders_collection = db["orders"]