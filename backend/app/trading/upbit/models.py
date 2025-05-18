"""
업비트 API 키 모델
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.base_class import Base

class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    exchange = Column(String, nullable=False)  # 거래소 이름 (예: upbit)
    access_key = Column(String, nullable=False)  # 암호화된 액세스 키
    secret_key = Column(String, nullable=False)  # 암호화된 시크릿 키
    is_active = Column(Boolean, default=True)  # 키 활성화 상태
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 