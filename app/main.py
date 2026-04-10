from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import category, product

app = FastAPI(
    title="Machine Test API",
    description="API for categories and products",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "FastAPI is working"}

Base.metadata.create_all(bind=engine)

app.include_router(category.router)
app.include_router(product.router)