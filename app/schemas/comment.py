from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
import uuid

class ReviewBase(BaseModel):
    product_id: uuid.UUID = Field(..., description="ID del producto reseñado")
    user_id: uuid.UUID = Field(..., description="ID del usuario que hace la reseña")
    reviewer_name: Optional[str] = Field(None, description="Nombre del reseñador")
    rating: int = Field(..., ge=1, le=5, description="Calificación de 1 a 5 estrellas")
    comment: str = Field(..., min_length=1, max_length=2000, description="Texto del comentario")
    
    @validator('rating')
    def validate_rating(cls, v):
        if v < 1 or v > 5:
            raise ValueError('El rating debe estar entre 1 y 5')
        return v

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    reviewer_name: Optional[str] = Field(None, description="Nombre del reseñador")
    rating: Optional[int] = Field(None, ge=1, le=5, description="Calificación de 1 a 5 estrellas")
    comment: Optional[str] = Field(None, min_length=1, max_length=2000, description="Texto del comentario")
    
    @validator('rating')
    def validate_rating(cls, v):
        if v is not None and (v < 1 or v > 5):
            raise ValueError('El rating debe estar entre 1 y 5')
        return v

class ReviewInDB(ReviewBase):
    id: uuid.UUID
    created_at: datetime
    
    class Config:
        from_attributes = True

class ReviewSchema(ReviewInDB):
    pass

# Schema para filtros de búsqueda
class ReviewFilter(BaseModel):
    product_id: Optional[uuid.UUID] = None
    user_id: Optional[uuid.UUID] = None
    rating: Optional[int] = Field(None, ge=1, le=5)

# Mantener alias para compatibilidad
CommentBase = ReviewBase
CommentCreate = ReviewCreate
CommentUpdate = ReviewUpdate
CommentInDB = ReviewInDB
CommentSchema = ReviewSchema
CommentFilter = ReviewFilter