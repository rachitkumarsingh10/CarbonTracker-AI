"""
Application Configuration
Loads environment variables and provides configuration settings
"""

from pydantic_settings import BaseSettings
from typing import List
import os
from pathlib import Path


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Application
    APP_NAME: str = "CarbonTracker AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    
    # Database (SQLite for local development)
    DATABASE_URL: str = "sqlite:///./carbontracker.db"
    
    # JWT Authentication
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # IBM watsonx.ai (Primary LLM)
    IBM_WATSONX_API_KEY: str = ""
    IBM_WATSONX_PROJECT_ID: str = ""
    IBM_WATSONX_URL: str = "https://us-south.ml.cloud.ibm.com"
    IBM_WATSONX_MODEL: str = "ibm/granite-13b-chat-v2"
    
    # Ollama (Fallback LLM)
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3"
    
    # ChromaDB
    CHROMA_HOST: str = "localhost"
    CHROMA_PORT: int = 8000
    CHROMA_COLLECTION_NAME: str = "sustainability_knowledge"
    USE_CHROMA_EMBEDDED: bool = True
    
    # OCR
    TESSERACT_PATH: str = "/usr/bin/tesseract"
    TESSERACT_LANG: str = "eng"
    
    # CORS
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:3001"
    CORS_ALLOW_CREDENTIALS: bool = True
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Get CORS origins as a list"""
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]
    
    # File Upload
    MAX_UPLOAD_SIZE: int = 10485760  # 10MB
    UPLOAD_DIR: str = "./uploads"
    ALLOWED_EXTENSIONS: str = "pdf,png,jpg,jpeg"
    
    @property
    def allowed_extensions_list(self) -> List[str]:
        """Get allowed extensions as a list"""
        return [ext.strip() for ext in self.ALLOWED_EXTENSIONS.split(",")]
    
    # Email (Optional)
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    EMAIL_FROM: str = "noreply@carbontracker.ai"
    
    # Redis (Optional)
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    
    # ML Model
    ML_MODEL_PATH: str = "./app/ml/models"
    PREDICTION_HORIZON_MONTHS: int = 6
    
    # Carbon Emission Factors (kg CO2)
    ELECTRICITY_FACTOR: float = 0.92  # per kWh
    CAR_FACTOR: float = 0.404  # per km
    PUBLIC_TRANSPORT_FACTOR: float = 0.089  # per km
    FLIGHT_FACTOR: float = 0.255  # per km
    MEAT_DIET_FACTOR: float = 7.2  # per day
    VEGETARIAN_DIET_FACTOR: float = 4.5  # per day
    VEGAN_DIET_FACTOR: float = 2.9  # per day
    WATER_FACTOR: float = 0.0003  # per liter
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
    @property
    def database_url_async(self) -> str:
        """Get async database URL"""
        if self.DATABASE_URL.startswith("postgresql://"):
            return self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
        return self.DATABASE_URL
    
    @property
    def chroma_url(self) -> str:
        """Get ChromaDB URL"""
        return f"http://{self.CHROMA_HOST}:{self.CHROMA_PORT}"
    
    @property
    def use_ibm_watsonx(self) -> bool:
        """Check if IBM watsonx.ai is configured"""
        return bool(self.IBM_WATSONX_API_KEY and self.IBM_WATSONX_PROJECT_ID)
    
    def get_upload_path(self) -> Path:
        """Get upload directory path"""
        path = Path(self.UPLOAD_DIR)
        path.mkdir(parents=True, exist_ok=True)
        return path
    
    def get_ml_model_path(self) -> Path:
        """Get ML model directory path"""
        path = Path(self.ML_MODEL_PATH)
        path.mkdir(parents=True, exist_ok=True)
        return path


# Create global settings instance
settings = Settings()


# Ensure required directories exist
settings.get_upload_path()
settings.get_ml_model_path()

# Made with Bob
