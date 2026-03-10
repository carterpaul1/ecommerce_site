from fastapi import FastAPI
from backend.routes import products, orders, auth, recommendations

app = FastAPI()

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(auth.router)
app.include_router(recommendations.router)

@app.get("/")
def root():
    return {"message": "E-commerce API running"}