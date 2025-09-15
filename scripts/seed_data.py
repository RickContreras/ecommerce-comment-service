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

def create_sample_comments():
    """Crear comentarios de ejemplo en la base de datos"""
    
    # IDs de productos reales del microservicio de productos
    sample_product_ids = [
        uuid.UUID("88d7984b-a03c-413c-960f-6bf99ef23291"),  # iPhone 15 Pro Max
        uuid.UUID("e377c7c7-fada-47c1-8607-c2a0b8e1375c"),  # MacBook Pro 14" M3
        uuid.UUID("2c45bd8c-87e5-42eb-b133-5f0fd8d7dd59"),  # AirPods Pro (3ª generación)
        uuid.UUID("0800be13-ba6f-4f1f-be05-d253bd756aa0"),  # Samsung Galaxy S24 Ultra
        uuid.UUID("c6dc5567-ecfa-4fbe-b2fb-c7399637f4fa"),  # Sony WH-1000XM5
        uuid.UUID("4dd6a4c5-44f2-8fa8-9a67-af2e6b6bc6cf"),  # Dell XPS 13 Plus
        uuid.UUID("e5a831b7-5b1b-480e-bac0-314703a572c5"),  # iPad Pro 12.9" M2
        uuid.UUID("b91a5b71-a435-4c90-9c88-884228bd4c50"),  # Nintendo Switch OLED
        uuid.UUID("14614427-6201-444a-af22-0fa0b4ad0ae0"),  # Apple Watch Series 9
        uuid.UUID("daeee192-320c-4c27-8c8c-5712eb706011"),  # Canon EOS R6 Mark II
    ]
    
    # IDs de usuarios de ejemplo
    sample_user_ids = [
        uuid.UUID("650e8400-e29b-41d4-a716-446655440000"),
        uuid.UUID("650e8400-e29b-41d4-a716-446655440001"),
        uuid.UUID("650e8400-e29b-41d4-a716-446655440002"),
        uuid.UUID("650e8400-e29b-41d4-a716-446655440003"),
        uuid.UUID("650e8400-e29b-41d4-a716-446655440004"),
        uuid.UUID("650e8400-e29b-41d4-a716-446655440005"),
        uuid.UUID("650e8400-e29b-41d4-a716-446655440006"),
        uuid.UUID("650e8400-e29b-41d4-a716-446655440007"),
        uuid.UUID("650e8400-e29b-41d4-a716-446655440008"),
        uuid.UUID("650e8400-e29b-41d4-a716-446655440009"),
    ]
    
    comments_data = [
        # Comentarios para iPhone 15 Pro Max
        {
            "content": "Excelente teléfono, la cámara es increíble y la batería dura todo el día. Muy recomendado.",
            "rating": 5,
            "product_id": sample_product_ids[0],
            "user_id": sample_user_ids[0],
            "author_name": "María González",
            "is_verified": True
        },
        {
            "content": "Buena calidad pero muy caro. La transición desde Android fue más difícil de lo esperado.",
            "rating": 4,
            "product_id": sample_product_ids[0],
            "user_id": sample_user_ids[1],
            "author_name": "Carlos Rodríguez",
            "is_verified": True
        },
        {
            "content": "El mejor iPhone hasta ahora. El titanio se siente premium y el rendimiento es sobresaliente.",
            "rating": 5,
            "product_id": sample_product_ids[0],
            "user_id": sample_user_ids[2],
            "author_name": "Ana López"
        },
        
        # Comentarios para MacBook Pro 14" M3
        {
            "content": "Perfecto para desarrollo de software. El chip M3 es una bestia y la pantalla es hermosa.",
            "rating": 5,
            "product_id": sample_product_ids[1],
            "user_id": sample_user_ids[3],
            "author_name": "David Martín",
            "is_verified": True
        },
        {
            "content": "Excelente laptop pero se calienta un poco con tareas muy intensivas. Por lo demás, perfecta.",
            "rating": 4,
            "product_id": sample_product_ids[1],
            "user_id": sample_user_ids[4],
            "author_name": "Laura Fernández"
        },
        
        # Comentarios para AirPods Pro (3ª generación)
        {
            "content": "La cancelación de ruido es impresionante. Perfectos para viajar y trabajar.",
            "rating": 5,
            "product_id": sample_product_ids[2],
            "user_id": sample_user_ids[5],
            "author_name": "Roberto Sánchez",
            "is_verified": True
        },
        {
            "content": "Buenos audífonos pero se me han caído varias veces. El estuche es un poco resbaladizo.",
            "rating": 3,
            "product_id": sample_product_ids[2],
            "user_id": sample_user_ids[0],
            "author_name": "Patricia Ruiz"
        },
        
        # Comentarios para Samsung Galaxy S24 Ultra
        {
            "content": "El S Pen es muy útil para tomar notas. La pantalla es vibrante y fluida.",
            "rating": 4,
            "product_id": sample_product_ids[3],
            "user_id": sample_user_ids[1],
            "author_name": "Miguel Torres",
            "is_verified": True
        },
        {
            "content": "Buena alternativa al iPhone. El sistema de cámaras es muy versátil.",
            "rating": 4,
            "product_id": sample_product_ids[3],
            "user_id": sample_user_ids[2],
            "author_name": "Elena Morales"
        },
        
        # Comentarios para Sony WH-1000XM5
        {
            "content": "Los mejores audífonos over-ear que he probado. La cancelación de ruido es excepcional.",
            "rating": 5,
            "product_id": sample_product_ids[4],
            "user_id": sample_user_ids[3],
            "author_name": "Alejandro Vega",
            "is_verified": True
        },
        {
            "content": "Excelente calidad de sonido pero un poco pesados para uso prolongado.",
            "rating": 4,
            "product_id": sample_product_ids[4],
            "user_id": sample_user_ids[4],
            "author_name": "Sandra Jiménez"
        },
        
        # Comentarios para Dell XPS 13 Plus
        {
            "content": "Laptop ultra delgada con excelente rendimiento. Perfecta para viajes de trabajo.",
            "rating": 5,
            "product_id": sample_product_ids[5],
            "user_id": sample_user_ids[5],
            "author_name": "Fernando Castro"
        },
        {
            "content": "Buena laptop pero la batería podría durar más. El teclado se siente premium.",
            "rating": 3,
            "product_id": sample_product_ids[5],
            "user_id": sample_user_ids[0],
            "author_name": "Carmen Ruiz"
        },
        
        # Comentarios para iPad Pro 12.9" M2
        {
            "content": "Increíble para diseño gráfico y edición de video. La pantalla es espectacular.",
            "rating": 5,
            "product_id": sample_product_ids[6],
            "user_id": sample_user_ids[1],
            "author_name": "Jorge Mendoza",
            "is_verified": True
        },
        {
            "content": "Muy buena tablet pero el precio es bastante alto para lo que ofrece.",
            "rating": 4,
            "product_id": sample_product_ids[6],
            "user_id": sample_user_ids[2],
            "author_name": "Lucía Herrera"
        },
        
        # Comentarios para Nintendo Switch OLED
        {
            "content": "La pantalla OLED se ve hermosa. Perfecto para jugar tanto en casa como en viajes.",
            "rating": 5,
            "product_id": sample_product_ids[7],
            "user_id": sample_user_ids[3],
            "author_name": "Ricardo Vargas",
            "is_verified": True
        },
        {
            "content": "Buenos juegos pero la consola se siente un poco frágil. Hay que cuidarla mucho.",
            "rating": 3,
            "product_id": sample_product_ids[7],
            "user_id": sample_user_ids[4],
            "author_name": "Andrea Silva"
        },
        
        # Comentarios para Apple Watch Series 9
        {
            "content": "Excelente para fitness y notificaciones. La batería dura todo el día sin problemas.",
            "rating": 5,
            "product_id": sample_product_ids[8],
            "user_id": sample_user_ids[5],
            "author_name": "Manuel Ortiz",
            "is_verified": True
        },
        {
            "content": "Bueno pero esperaba más funciones para el precio que tiene. Es muy básico.",
            "rating": 3,
            "product_id": sample_product_ids[8],
            "user_id": sample_user_ids[0],
            "author_name": "Valentina Cruz"
        },
        
        # Comentarios para Canon EOS R6 Mark II
        {
            "content": "Cámara profesional increíble. Las fotos salen con una calidad impresionante.",
            "rating": 5,
            "product_id": sample_product_ids[9],
            "user_id": sample_user_ids[1],
            "author_name": "Sebastián Torres",
            "is_verified": True
        },
        {
            "content": "Excelente cámara pero muy cara. Solo recomendable para fotógrafos profesionales.",
            "rating": 4,
            "product_id": sample_product_ids[9],
            "user_id": sample_user_ids[2],
            "author_name": "Isabella Rojas"
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
            print("❌ Ya existen comentarios en la base de datos. Saltando la creación de datos de ejemplo.")
            return
        
        print("🌱 Creando comentarios de ejemplo...")
        
        # Crear comentarios
        comments_data = create_sample_comments()
        created_count = 0
        
        for comment_data in comments_data:
            # Añadir timestamps realistas (comentarios de los últimos 6 meses)
            days_ago = random.randint(1, 180)
            created_at = datetime.now(timezone.utc) - timedelta(days=days_ago)
            
            comment = Comment(
                **comment_data,
                created_at=created_at,
                updated_at=created_at
            )
            
            db.add(comment)
            created_count += 1
        
        db.commit()
        print(f"✅ Se crearon {created_count} comentarios de ejemplo exitosamente.")
        
        # Mostrar estadísticas
        total_comments = db.query(Comment).count()
        verified_comments = db.query(Comment).filter(Comment.is_verified == True).count()
        avg_rating = db.query(func.avg(Comment.rating)).scalar()
        
        print(f"\n📊 Estadísticas de la base de datos:")
        print(f"   • Total de comentarios: {total_comments}")
        print(f"   • Comentarios verificados: {verified_comments}")
        print(f"   • Calificación promedio: {avg_rating:.2f}/5.0" if avg_rating else "   • Calificación promedio: N/A")
        
    except Exception as e:
        print(f"❌ Error al crear comentarios de ejemplo: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("🚀 Iniciando creación de datos de ejemplo para el servicio de comentarios...")
    seed_comments_data()
    print("🎉 Proceso completado.")