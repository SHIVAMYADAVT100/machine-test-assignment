from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate

router = APIRouter(prefix="/api/products", tags=["Products"])

# Get all products
@router.get("")
def get_products(page: int = 1, db: Session = Depends(get_db)):
    limit = 5
    skip = (page - 1) * limit
    return db.query(Product).offset(skip).limit(limit).all()

# Create product
@router.post("")
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    product = Product(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Get product by id
@router.get("/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.id == id).first()

# Update product
@router.put("/{id}")
def update_product(id: int, data: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    for key, value in data.dict().items():
        setattr(product, key, value)
    db.commit()
    return product

# Delete product
@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    db.delete(product)
    db.commit()
    return {"message": "Deleted"}
