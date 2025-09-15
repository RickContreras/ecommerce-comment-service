from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
import uuid

class CommentBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=2000)
    rating: Optional[int] = Field(None, ge=1, le=5)
    product_id: uuid.UUID = Field(..., description="ID del producto comentado")
    user_id: uuid.UUID = Field(..., description="ID del usuario que comenta")
    author_name: Optional[str] = Field(None, max_length=255)
    
    @validator('rating')
    def validate_rating(cls, v):
        if v is not None and (v < 1 or v > 5):
            raise ValueError('El rating debe estar entre 1 y 5')
        return v

class CommentCreate(CommentBase):
    pass

class CommentUpdate(BaseModel):
    content: Optional[str] = Field(None, min_length=1, max_length=2000)
    rating: Optional[int] = Field(None, ge=1, le=5)
    author_name: Optional[str] = Field(None, max_length=255)
    is_active: Optional[bool] = Field(None)
    
    @validator('rating')
    def validate_rating(cls, v):
        if v is not None and (v < 1 or v > 5):
            raise ValueError('El rating debe estar entre 1 y 5')
        return v

class CommentInDB(CommentBase):
    id: uuid.UUID
    is_verified: bool
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True

class CommentSchema(CommentInDB):
    pass

# Schema para filtros de búsqueda
class CommentFilter(BaseModel):
    product_id: Optional[uuid.UUID] = None
    user_id: Optional[uuid.UUID] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    is_verified: Optional[bool] = None
    is_active: Optional[bool] = True