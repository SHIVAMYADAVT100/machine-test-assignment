from pydantic import BaseModel
from app.schemas.category import CategoryResponse

class ProductCreate(BaseModel):
    name: str
    description: str
    category_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    category: CategoryResponse

    class Config:
        orm_mode = True