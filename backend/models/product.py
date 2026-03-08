from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class Product(BaseModel):
    name: str
    description: str
    price: float
    category: str
    image: str
    stock: int

class ProductResponse(Product):
    id: Optional[str]