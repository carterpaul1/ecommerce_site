from fastapi import APIRouter
from backend.database import orders_collection, products_collection
from bson import ObjectId
from datetime import datetime

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


# Create order (checkout)
@router.post("/")
def create_order(order: dict):

    items = order["items"]
    user_id = order["user_id"]

    total = 0

    for item in items:

        print("Looking up product:", item["product_id"])

        product = products_collection.find_one(
            {"_id": ObjectId(item["product_id"])}
        )

        if not product:
            return {"error": f"Product not found: {item['product_id']}"}

        price = product["price"]
        quantity = item["quantity"]

        total += price * quantity

        item["name"] = product["name"]
        item["price"] = price

    new_order = {
        "user_id": user_id,
        "items": items,
        "total": total,
        "created_at": datetime.utcnow()
    }

    result = orders_collection.insert_one(new_order)

    return {
        "order_id": str(result.inserted_id),
        "total": total
    }


# Get user orders
@router.get("/{user_id}")
def get_orders(user_id: str):

    orders = []

    for order in orders_collection.find({"user_id": user_id}):

        order["id"] = str(order["_id"])
        del order["_id"]

        orders.append(order)

    return orders