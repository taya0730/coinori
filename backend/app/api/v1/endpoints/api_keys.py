"""
API 키 관리 엔드포인트
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.trading.upbit.services import ApiKeyService
from app.trading.upbit.models import ApiKey
from app.trading.upbit.exceptions import UpbitAPIKeyError
from app.trading.upbit.schemas import ApiKey as ApiKeySchema, ApiKeyCreate, ApiKeyUpdateStatus

router = APIRouter()

@router.post("/", response_model=ApiKeySchema)
def create_api_key(
    api_key: ApiKeyCreate,
    db: Session = Depends(deps.get_db)
):
    """
    새로운 API 키 생성
    """
    try:
        api_key_service = ApiKeyService(db)
        return api_key_service.create_api_key(
            api_key.exchange,
            api_key.access_key,
            api_key.secret_key
        )
    except UpbitAPIKeyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[ApiKeySchema])
def get_api_keys(
    exchange: str,
    db: Session = Depends(deps.get_db)
):
    """
    활성화된 API 키 목록 조회
    """
    try:
        api_key_service = ApiKeyService(db)
        return api_key_service.get_active_api_keys(exchange)
    except UpbitAPIKeyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{key_id}", response_model=ApiKeySchema)
def get_api_key(
    key_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    특정 API 키 조회
    """
    try:
        api_key_service = ApiKeyService(db)
        api_key = api_key_service.get_api_key(key_id)
        if not api_key:
            raise HTTPException(status_code=404, detail="API 키를 찾을 수 없습니다.")
        return api_key
    except UpbitAPIKeyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{key_id}/status")
def update_api_key_status(
    key_id: int,
    status: ApiKeyUpdateStatus,
    db: Session = Depends(deps.get_db)
):
    """
    API 키 활성화 상태 업데이트
    """
    try:
        api_key_service = ApiKeyService(db)
        api_key = api_key_service.update_api_key_status(key_id, status.is_active)
        if not api_key:
            raise HTTPException(status_code=404, detail="API 키를 찾을 수 없습니다.")
        return {"message": "API 키 상태가 업데이트되었습니다."}
    except UpbitAPIKeyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{key_id}")
def delete_api_key(
    key_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    API 키 삭제
    """
    try:
        api_key_service = ApiKeyService(db)
        if not api_key_service.delete_api_key(key_id):
            raise HTTPException(status_code=404, detail="API 키를 찾을 수 없습니다.")
        return {"message": "API 키가 삭제되었습니다."}
    except UpbitAPIKeyError as e:
        raise HTTPException(status_code=400, detail=str(e)) 