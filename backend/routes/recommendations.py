from fastapi import APIRouter
from services.recommendation_engine import recommend_products

router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"]
)

@router.get("/{user_id}")
def get_recommendations(user_id: str):

    products = recommend_products(user_id)

    return {"recommendations": products}