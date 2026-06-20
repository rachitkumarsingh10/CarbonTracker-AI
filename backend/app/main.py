"""
CarbonTracker AI - Main Application
FastAPI application with AI-powered carbon footprint tracking
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

from app.core.config import settings
from app.core.database import init_db

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered carbon footprint tracking and analysis platform",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """
    Application startup event
    Initialize database and services
    """
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    
    # Initialize database
    try:
        init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
    
    # Log configuration
    logger.info(f"Debug mode: {settings.DEBUG}")
    logger.info(f"Using IBM watsonx.ai: {settings.use_ibm_watsonx}")
    logger.info(f"ChromaDB URL: {settings.chroma_url}")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Application shutdown event
    Cleanup resources
    """
    logger.info(f"Shutting down {settings.APP_NAME}")


@app.get("/")
async def root():
    """
    Root endpoint
    Returns API information
    """
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    Returns application health status
    """
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG
    }


@app.get("/api/v1/info")
async def api_info():
    """
    API information endpoint
    Returns API configuration details
    """
    return {
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "llm_provider": "IBM watsonx.ai" if settings.use_ibm_watsonx else "Ollama",
        "features": {
            "carbon_calculator": True,
            "ai_chatbot": True,
            "rag_system": True,
            "ml_predictions": True,
            "ocr_upload": True,
            "analytics": True
        }
    }


# Import and include routers
from app.api import carbon, analytics

app.include_router(carbon.router, prefix="/api/carbon", tags=["Carbon Calculator"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])

# Additional routers (to be created)
# from app.api import auth, users, analytics, chat, recommendations, predictions, documents, admin
# app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
# app.include_router(users.router, prefix="/api/users", tags=["Users"])
# app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
# app.include_router(chat.router, prefix="/api/chat", tags=["AI Chat"])
# app.include_router(recommendations.router, prefix="/api/recommendations", tags=["Recommendations"])
# app.include_router(predictions.router, prefix="/api/predictions", tags=["Predictions"])
# app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
# app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])


# Exception handlers
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """
    Global exception handler
    Catches all unhandled exceptions
    """
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "message": str(exc) if settings.DEBUG else "An error occurred"
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )

# Made with Bob
