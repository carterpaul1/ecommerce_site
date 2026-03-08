from fastapi import APIRouter
from database import products_collection
from bson import ObjectId

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

# Get all products
@router.get("/")
def get_products():

    products = []

    for product in products_collection.find():
        product["id"] = str(product["_id"])
        del product["_id"]
        products.append(product)

    return products


# Get single product
@router.get("/{product_id}")
def get_product(product_id: str):

    product = products_collection.find_one({"_id": ObjectId(product_id)})

    if product:
        product["id"] = str(product["_id"])
        del product["_id"]
        return product

    return {"error": "Product not found"}


# Create product
@router.post("/")
def create_product(product: dict):

    result = products_collection.insert_one(product)

    return {"product_id": str(result.inserted_id)}


# Update product
@router.put("/{product_id}")
def update_product(product_id: str, product: dict):

    products_collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": product}
    )

    return {"message": "Product updated"}


# Delete product
@router.delete("/{product_id}")
def delete_product(product_id: str):

    products_collection.delete_one({"_id": ObjectId(product_id)})

    return {"message": "Product deleted"}