from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.endpoints.comments import router as comment_router

app = FastAPI(
    title="Ecommerce Comment Service",
    version=settings.api_version,
    description="Microservicio para gestión de comentarios y reseñas",
    debug=settings.debug
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(comment_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Ecommerce Comment Service API", "version": settings.api_version}

@app.get("/health")
def health_check():
    return {"status": "healthy"}