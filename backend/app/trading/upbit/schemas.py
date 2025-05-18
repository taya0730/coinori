"""
API 키 관련 스키마
"""

from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class ApiKeyBase(BaseModel):
    """API 키 기본 스키마"""
    exchange: str
    access_key: str
    secret_key: str

class ApiKeyCreate(ApiKeyBase):
    """API 키 생성 스키마"""
    pass

class ApiKeyUpdateStatus(BaseModel):
    """API 키 상태 업데이트 스키마"""
    is_active: bool

class ApiKeyInDBBase(ApiKeyBase):
    """API 키 데이터베이스 스키마"""
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ApiKey(ApiKeyInDBBase):
    """API 키 응답 스키마"""
    pass 