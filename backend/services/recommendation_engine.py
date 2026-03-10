from collections import Counter
from backend.database import orders_collection, products_collection

def recommend_products(user_id: str):

    # Get user orders
    user_orders = orders_collection.find({"user_id": user_id})

    purchased_products = []

    for order in user_orders:
        for item in order["items"]:
            purchased_products.append(item["product_id"])

    if not purchased_products:
        # If user has no purchases return popular items
        return list(products_collection.find().limit(5))

    # Find orders that contain same products
    similar_orders = orders_collection.find({
        "items.product_id": {"$in": purchased_products}
    })

    recommended = []

    for order in similar_orders:
        for item in order["items"]:
            recommended.append(item["product_id"])

    counts = Counter(recommended)

    # Remove items user already purchased
    for p in purchased_products:
        counts.pop(p, None)

    # Get top recommended product IDs
    top_products = [pid for pid, count in counts.most_common(5)]

    recommendations = list(products_collection.find({
        "_id": {"$in": top_products}
    }))

    return recommendations