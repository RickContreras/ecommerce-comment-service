from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentUpdate, CommentFilter
from typing import List, Optional
import uuid

class CommentCRUD:
    def create(self, db: Session, comment_data: CommentCreate) -> Comment:
        db_comment = Comment(**comment_data.dict())
        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)
        return db_comment
    
    def get(self, db: Session, comment_id: uuid.UUID) -> Optional[Comment]:
        return db.query(Comment).filter(Comment.id == comment_id).first()
    
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[Comment]:
        return db.query(Comment).offset(skip).limit(limit).all()
    
    def get_by_product(self, db: Session, product_id: uuid.UUID, skip: int = 0, limit: int = 100) -> List[Comment]:
        return db.query(Comment).filter(Comment.product_id == product_id).offset(skip).limit(limit).all()
    
    def get_by_user(self, db: Session, user_id: uuid.UUID, skip: int = 0, limit: int = 100) -> List[Comment]:
        return db.query(Comment).filter(Comment.user_id == user_id).offset(skip).limit(limit).all()
    
    def get_with_filters(self, db: Session, filters: CommentFilter, skip: int = 0, limit: int = 100) -> List[Comment]:
        query = db.query(Comment)
        
        if filters.product_id:
            query = query.filter(Comment.product_id == filters.product_id)
        if filters.user_id:
            query = query.filter(Comment.user_id == filters.user_id)
        if filters.rating:
            query = query.filter(Comment.rating == filters.rating)
            
        return query.offset(skip).limit(limit).all()
    
    def update(self, db: Session, comment_id: uuid.UUID, comment_data: CommentUpdate) -> Optional[Comment]:
        db_comment = self.get(db, comment_id)
        if not db_comment:
            return None
        
        update_data = comment_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_comment, key, value)
        
        db.commit()
        db.refresh(db_comment)
        return db_comment
    
    def delete(self, db: Session, comment_id: uuid.UUID) -> bool:
        """Hard delete - elimina permanentemente el comentario"""
        db_comment = self.get(db, comment_id)
        if not db_comment:
            return False
        
        db.delete(db_comment)
        db.commit()
        return True
    
    def soft_delete(self, db: Session, comment_id: uuid.UUID) -> bool:
        """Soft delete - como no tenemos campo is_active, implementamos como hard delete"""
        return self.delete(db, comment_id)
    
    def get_average_rating(self, db: Session, product_id: uuid.UUID) -> Optional[float]:
        """Obtiene el rating promedio de un producto"""
        from sqlalchemy import func
        result = db.query(func.avg(Comment.rating)).filter(
            Comment.product_id == product_id
        ).scalar()
        return float(result) if result else None
    
    def get_comment_count(self, db: Session, product_id: uuid.UUID) -> int:
        """Obtiene el número total de comentarios de un producto"""
        return db.query(Comment).filter(Comment.product_id == product_id).count()