from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.category import Category
from app.schemas.category import CategoryCreate

router = APIRouter(prefix="/api/categories", tags=["Categories"])

# Get all categories
@router.get("")
def get_categories(page: int = 1, db: Session = Depends(get_db)):
    limit = 5
    skip = (page - 1) * limit
    return db.query(Category).offset(skip).limit(limit).all()

# Create category
@router.post("")
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    category = Category(name=data.name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

# Get category by id
@router.get("/{id}")
def get_category(id: int, db: Session = Depends(get_db)):
    return db.query(Category).filter(Category.id == id).first()

# Update category
@router.put("/{id}")
def update_category(id: int, data: CategoryCreate, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    category.name = data.name
    db.commit()
    return category

# Delete category
@router.delete("/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    db.delete(category)
    db.commit()
    return {"message": "Deleted"}
