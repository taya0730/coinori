"""
API 라우터
"""

from fastapi import APIRouter
from app.api.v1.endpoints import api_keys

api_router = APIRouter()
api_router.include_router(api_keys.router, prefix="/api-keys", tags=["api-keys"]) 