"""
업비트 API 키 관리 서비스
"""

from typing import Optional, List
from sqlalchemy.orm import Session
from app.core.security import CryptoUtils
from .models import ApiKey
from .exceptions import UpbitAPIKeyError

class ApiKeyService:
    def __init__(self, db: Session):
        """
        API 키 서비스 초기화
        
        Args:
            db (Session): 데이터베이스 세션
        """
        self.db = db
        self.crypto = CryptoUtils()
    
    def create_api_key(self, exchange: str, access_key: str, secret_key: str) -> ApiKey:
        """
        새로운 API 키 생성
        
        Args:
            exchange (str): 거래소 이름
            access_key (str): 액세스 키
            secret_key (str): 시크릿 키
            
        Returns:
            ApiKey: 생성된 API 키 객체
        """
        try:
            # API 키 암호화
            encrypted_access_key = self.crypto.encrypt(access_key)
            encrypted_secret_key = self.crypto.encrypt(secret_key)
            
            # 데이터베이스에 저장
            api_key = ApiKey(
                exchange=exchange,
                access_key=encrypted_access_key,
                secret_key=encrypted_secret_key,
                is_active=True
            )
            self.db.add(api_key)
            self.db.commit()
            self.db.refresh(api_key)
            return api_key
        except Exception as e:
            self.db.rollback()
            raise UpbitAPIKeyError(f"API 키 생성 실패: {str(e)}")
    
    def get_api_key(self, key_id: int) -> Optional[ApiKey]:
        """
        API 키 조회
        
        Args:
            key_id (int): API 키 ID
            
        Returns:
            Optional[ApiKey]: API 키 객체 또는 None
        """
        return self.db.query(ApiKey).filter(ApiKey.id == key_id).first()
    
    def get_active_api_keys(self, exchange: str) -> List[ApiKey]:
        """
        활성화된 API 키 목록 조회
        
        Args:
            exchange (str): 거래소 이름
            
        Returns:
            List[ApiKey]: API 키 객체 목록
        """
        return self.db.query(ApiKey).filter(
            ApiKey.exchange == exchange,
            ApiKey.is_active == True
        ).all()
    
    def update_api_key_status(self, key_id: int, is_active: bool) -> Optional[ApiKey]:
        """
        API 키 활성화 상태 업데이트
        
        Args:
            key_id (int): API 키 ID
            is_active (bool): 활성화 상태
            
        Returns:
            Optional[ApiKey]: 업데이트된 API 키 객체 또는 None
        """
        try:
            api_key = self.get_api_key(key_id)
            if not api_key:
                return None
            
            api_key.is_active = is_active
            self.db.commit()
            self.db.refresh(api_key)
            return api_key
        except Exception as e:
            self.db.rollback()
            raise UpbitAPIKeyError(f"API 키 상태 업데이트 실패: {str(e)}")
    
    def delete_api_key(self, key_id: int) -> bool:
        """
        API 키 삭제
        
        Args:
            key_id (int): API 키 ID
            
        Returns:
            bool: 삭제 성공 여부
        """
        try:
            api_key = self.get_api_key(key_id)
            if not api_key:
                return False
            
            self.db.delete(api_key)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise UpbitAPIKeyError(f"API 키 삭제 실패: {str(e)}")
    
    def get_decrypted_keys(self, key_id: int) -> tuple[str, str]:
        """
        복호화된 API 키 조회
        
        Args:
            key_id (int): API 키 ID
            
        Returns:
            tuple[str, str]: (액세스 키, 시크릿 키)
        """
        api_key = self.get_api_key(key_id)
        if not api_key:
            raise UpbitAPIKeyError("API 키를 찾을 수 없습니다.")
        
        try:
            access_key = self.crypto.decrypt(api_key.access_key)
            secret_key = self.crypto.decrypt(api_key.secret_key)
            return access_key, secret_key
        except Exception as e:
            raise UpbitAPIKeyError(f"API 키 복호화 실패: {str(e)}") 