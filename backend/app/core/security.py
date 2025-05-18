from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
from typing import Tuple

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None

class CryptoUtils:
    def __init__(self, secret_key: str = None):
        """
        암호화 유틸리티 초기화
        
        Args:
            secret_key (str, optional): 암호화에 사용할 비밀 키. 
                                      제공되지 않으면 환경 변수에서 가져옴
        """
        if secret_key is None:
            secret_key = os.getenv("ENCRYPTION_KEY")
            if not secret_key:
                raise ValueError("암호화 키가 설정되지 않았습니다.")
        
        # PBKDF2를 사용하여 키 생성
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'coinori_salt',  # 실제 운영에서는 환경 변수로 관리
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(secret_key.encode()))
        self.fernet = Fernet(key)
    
    def encrypt(self, text: str) -> str:
        """
        문자열 암호화
        
        Args:
            text (str): 암호화할 문자열
            
        Returns:
            str: 암호화된 문자열
        """
        return self.fernet.encrypt(text.encode()).decode()
    
    def decrypt(self, encrypted_text: str) -> str:
        """
        문자열 복호화
        
        Args:
            encrypted_text (str): 복호화할 문자열
            
        Returns:
            str: 복호화된 문자열
        """
        return self.fernet.decrypt(encrypted_text.encode()).decode()
    
    @staticmethod
    def generate_key() -> str:
        """
        새로운 암호화 키 생성
        
        Returns:
            str: 생성된 암호화 키
        """
        return Fernet.generate_key().decode()
