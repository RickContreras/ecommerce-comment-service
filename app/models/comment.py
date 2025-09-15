from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    content = Column(Text, nullable=False)
    rating = Column(Integer, nullable=True)  # Rating 1-5 stars
    product_id = Column(UUID(as_uuid=True), nullable=False, index=True)  # ID del producto comentado
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)  # ID del usuario que comenta
    author_name = Column(String(255), nullable=True)  # Nombre del autor (opcional)
    is_verified = Column(Boolean, default=False)  # Si la compra está verificada
    is_active = Column(Boolean, default=True)  # Si el comentario está activo/visible
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())