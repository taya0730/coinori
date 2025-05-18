from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Coinori"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/coinori")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]
    
    # Exchange API Settings
    BINANCE_API_URL: str = "https://api.binance.com"
    UPBIT_API_URL: str = "https://api.upbit.com"
    
    # Trading Settings
    DEFAULT_TRADE_AMOUNT: float = 0.001  # BTC
    MAX_TRADE_AMOUNT: float = 0.1  # BTC
    DEFAULT_STOP_LOSS: float = 2.0  # percentage
    DEFAULT_TAKE_PROFIT: float = 4.0  # percentage
    
    class Config:
        case_sensitive = True

settings = Settings()
