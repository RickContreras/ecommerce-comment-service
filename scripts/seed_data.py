#!/usr/bin/env python3
"""
Script para poblar la base de datos con comentarios de ejemplo
"""
import sys
import os
import uuid
from datetime import datetime, timedelta, timezone
import random

# Agregar el directorio raíz al path para importar módulos de la app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import SessionLocal
from app.models.comment import Comment

def seed_comments():
    """Seed the database with sample comments."""
    # Sample product UUIDs - estos deberían corresponder a productos reales en tu base de datos de productos
    sample_product_ids = [
        uuid.UUID("01234567-89ab-cdef-0123-456789abcdef"),  # iPhone 15 Pro Max
        uuid.UUID("11234567-89ab-cdef-0123-456789abcdef"),  # MacBook Pro 14" M3
        uuid.UUID("21234567-89ab-cdef-0123-456789abcdef"),  # AirPods Pro (3ª generación)
        uuid.UUID("31234567-89ab-cdef-0123-456789abcdef"),  # Samsung Galaxy S24 Ultra
        uuid.UUID("41234567-89ab-cdef-0123-456789abcdef"),  # Sony WH-1000XM5
        uuid.UUID("51234567-89ab-cdef-0123-456789abcdef"),  # Dell XPS 13 Plus
        uuid.UUID("61234567-89ab-cdef-0123-456789abcdef"),  # iPad Pro 12.9" M2
        uuid.UUID("71234567-89ab-cdef-0123-456789abcdef"),  # Nintendo Switch OLED
        uuid.UUID("81234567-89ab-cdef-0123-456789abcdef"),  # Apple Watch Series 9
        uuid.UUID("91234567-89ab-cdef-0123-456789abcdef"),  # Canon EOS R6 Mark II
    ]
    
    # Sample user UUIDs - estos deberían corresponder a usuarios reales en tu base de datos de usuarios
    sample_user_ids = [
        uuid.UUID("a0234567-89ab-cdef-0123-456789abcdef"),  # María González
        uuid.UUID("a1234567-89ab-cdef-0123-456789abcdef"),  # Carlos Rodríguez
        uuid.UUID("a2234567-89ab-cdef-0123-456789abcdef"),  # Ana López
        uuid.UUID("a3234567-89ab-cdef-0123-456789abcdef"),  # David Martín
        uuid.UUID("a4234567-89ab-cdef-0123-456789abcdef"),  # Laura Fernández
        uuid.UUID("a5234567-89ab-cdef-0123-456789abcdef"),  # Roberto Sánchez
    ]
    
    comments_data = [
        # Comentarios para iPhone 15 Pro Max
        {
            "comment": "Excelente teléfono, la cámara es increíble y la batería dura todo el día. Muy recomendado.",
            "rating": 5,
            "product_id": sample_product_ids[0],
            "user_id": sample_user_ids[0],
            "reviewer_name": "María González"
        },
        {
            "comment": "Buena calidad pero muy caro. La transición desde Android fue más difícil de lo esperado.",
            "rating": 4,
            "product_id": sample_product_ids[0],
            "user_id": sample_user_ids[1],
            "reviewer_name": "Carlos Rodríguez"
        },
        {
            "comment": "El mejor iPhone hasta ahora. El titanio se siente premium y el rendimiento es sobresaliente.",
            "rating": 5,
            "product_id": sample_product_ids[0],
            "user_id": sample_user_ids[2],
            "reviewer_name": "Ana López"
        },
        
        # Comentarios para MacBook Pro 14" M3
        {
            "comment": "Perfecto para desarrollo de software. El chip M3 es una bestia y la pantalla es hermosa.",
            "rating": 5,
            "product_id": sample_product_ids[1],
            "user_id": sample_user_ids[3],
            "reviewer_name": "David Martín"
        },
        {
            "comment": "Excelente laptop pero se calienta un poco con tareas muy intensivas. Por lo demás, perfecta.",
            "rating": 4,
            "product_id": sample_product_ids[1],
            "user_id": sample_user_ids[4],
            "reviewer_name": "Laura Fernández"
        },
        
        # Comentarios para AirPods Pro (3ª generación)
        {
            "comment": "La cancelación de ruido es impresionante. Perfectos para viajar y trabajar.",
            "rating": 5,
            "product_id": sample_product_ids[2],
            "user_id": sample_user_ids[5],
            "reviewer_name": "Roberto Sánchez"
        },
        {
            "comment": "Buenos audífonos pero se me han caído varias veces. El estuche es un poco resbaladizo.",
            "rating": 3,
            "product_id": sample_product_ids[2],
            "user_id": sample_user_ids[0],
            "reviewer_name": "Patricia Ruiz"
        },
        
        # Comentarios para Samsung Galaxy S24 Ultra
        {
            "comment": "El S Pen es muy útil para tomar notas. La pantalla es vibrante y fluida.",
            "rating": 4,
            "product_id": sample_product_ids[3],
            "user_id": sample_user_ids[1],
            "reviewer_name": "Miguel Torres"
        },
        {
            "comment": "Buena alternativa al iPhone. El sistema de cámaras es muy versátil.",
            "rating": 4,
            "product_id": sample_product_ids[3],
            "user_id": sample_user_ids[2],
            "reviewer_name": "Elena Morales"
        },
        
        # Comentarios para Sony WH-1000XM5
        {
            "comment": "Los mejores audífonos over-ear que he probado. La cancelación de ruido es excepcional.",
            "rating": 5,
            "product_id": sample_product_ids[4],
            "user_id": sample_user_ids[3],
            "reviewer_name": "Alejandro Vega"
        },
        {
            "comment": "Excelente calidad de sonido pero un poco pesados para uso prolongado.",
            "rating": 4,
            "product_id": sample_product_ids[4],
            "user_id": sample_user_ids[4],
            "reviewer_name": "Sandra Jiménez"
        },
        
        # Comentarios para Dell XPS 13 Plus
        {
            "comment": "Laptop ultra delgada con excelente rendimiento. Perfecta para viajes de trabajo.",
            "rating": 5,
            "product_id": sample_product_ids[5],
            "user_id": sample_user_ids[5],
            "reviewer_name": "Fernando Castro"
        },
        {
            "comment": "Buena laptop pero la batería podría durar más. El teclado se siente premium.",
            "rating": 3,
            "product_id": sample_product_ids[5],
            "user_id": sample_user_ids[0],
            "reviewer_name": "Carmen Ruiz"
        },
        
        # Comentarios para iPad Pro 12.9" M2
        {
            "comment": "Increíble para diseño gráfico y edición de video. La pantalla es espectacular.",
            "rating": 5,
            "product_id": sample_product_ids[6],
            "user_id": sample_user_ids[1],
            "reviewer_name": "Jorge Mendoza"
        },
        {
            "comment": "Muy buena tablet pero el precio es bastante alto para lo que ofrece.",
            "rating": 4,
            "product_id": sample_product_ids[6],
            "user_id": sample_user_ids[2],
            "reviewer_name": "Lucía Herrera"
        },
        
        # Comentarios para Nintendo Switch OLED
        {
            "comment": "La pantalla OLED se ve hermosa. Perfecto para jugar tanto en casa como en viajes.",
            "rating": 5,
            "product_id": sample_product_ids[7],
            "user_id": sample_user_ids[3],
            "reviewer_name": "Ricardo Vargas"
        },
        {
            "comment": "Buenos juegos pero la consola se siente un poco frágil. Hay que cuidarla mucho.",
            "rating": 3,
            "product_id": sample_product_ids[7],
            "user_id": sample_user_ids[4],
            "reviewer_name": "Andrea Silva"
        },
        
        # Comentarios para Apple Watch Series 9
        {
            "comment": "Excelente para fitness y notificaciones. La batería dura todo el día sin problemas.",
            "rating": 5,
            "product_id": sample_product_ids[8],
            "user_id": sample_user_ids[5],
            "reviewer_name": "Manuel Ortiz"
        },
        {
            "comment": "Bueno pero esperaba más funciones para el precio que tiene. Es muy básico.",
            "rating": 3,
            "product_id": sample_product_ids[8],
            "user_id": sample_user_ids[0],
            "reviewer_name": "Valentina Cruz"
        },
        
        # Comentarios para Canon EOS R6 Mark II
        {
            "comment": "Cámara profesional increíble. Las fotos salen con una calidad impresionante.",
            "rating": 5,
            "product_id": sample_product_ids[9],
            "user_id": sample_user_ids[1],
            "reviewer_name": "Sebastián Torres"
        },
        {
            "comment": "Excelente cámara pero muy cara. Solo recomendable para fotógrafos profesionales.",
            "rating": 4,
            "product_id": sample_product_ids[9],
            "user_id": sample_user_ids[2],
            "reviewer_name": "Isabella Rojas"
        }
    ]
    
    return comments_data

def seed_comments_data():
    """Función principal para poblar la base de datos con comentarios de ejemplo"""
    db = SessionLocal()
    try:
        # Verificar si ya existen comentarios
        existing_comments = db.query(Comment).first()
        if existing_comments:
            print("❌ Ya existen reseñas en la base de datos. Saltando la creación de datos de ejemplo.")
            return
        
        print("🌱 Creando reseñas de ejemplo...")
        
        # Crear comentarios
        comments_data = seed_comments()
        created_count = 0
        
        for comment_data in comments_data:
            # Añadir timestamps realistas (comentarios de los últimos 6 meses)
            days_ago = random.randint(1, 180)
            created_at = datetime.now(timezone.utc) - timedelta(days=days_ago)
            
            comment = Comment(
                **comment_data,
                created_at=created_at
            )
            
            db.add(comment)
            created_count += 1
        
        db.commit()
        print(f"✅ Se crearon {created_count} reseñas de ejemplo exitosamente.")
        
        # Mostrar estadísticas
        total_comments = db.query(Comment).count()
        avg_rating = db.query(func.avg(Comment.rating)).scalar()
        
        print(f"\n📊 Estadísticas de la base de datos:")
        print(f"   • Total de reseñas: {total_comments}")
        print(f"   • Calificación promedio: {avg_rating:.2f}/5.0" if avg_rating else "   • Calificación promedio: N/A")
        
    except Exception as e:
        print(f"❌ Error al crear comentarios de ejemplo: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("🚀 Iniciando creación de datos de ejemplo para el servicio de reseñas...")
    seed_comments_data()
    print("🎉 Proceso completado.")