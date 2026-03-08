from fastapi import FastAPI
from routes import auth, products, orders, recommendations

app = FastAPI()

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(recommendations.router)

@app.get("/")
def home():
    return {"message": "Ecommerce API running"}