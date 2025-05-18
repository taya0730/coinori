"""
API 키 엔드포인트 테스트
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.trading.upbit.models import ApiKey

def test_create_api_key(client: TestClient, db):
    """API 키 생성 테스트"""
    response = client.post(
        "/api/v1/api-keys/",
        json={
            "exchange": "upbit",
            "access_key": "test-access-key",
            "secret_key": "test-secret-key"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["exchange"] == "upbit"
    assert data["is_active"] is True
    assert "access_key" in data
    assert "secret_key" in data

def test_get_api_keys(client: TestClient, db):
    """API 키 목록 조회 테스트"""
    # 먼저 API 키 생성
    client.post(
        "/api/v1/api-keys/",
        json={
            "exchange": "upbit",
            "access_key": "test-access-key",
            "secret_key": "test-secret-key"
        }
    )
    
    # API 키 목록 조회
    response = client.get("/api/v1/api-keys/", params={"exchange": "upbit"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["exchange"] == "upbit"

def test_get_api_key(client: TestClient, db):
    """특정 API 키 조회 테스트"""
    # 먼저 API 키 생성
    create_response = client.post(
        "/api/v1/api-keys/",
        json={
            "exchange": "upbit",
            "access_key": "test-access-key",
            "secret_key": "test-secret-key"
        }
    )
    key_id = create_response.json()["id"]
    
    # 특정 API 키 조회
    response = client.get(f"/api/v1/api-keys/{key_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == key_id
    assert data["exchange"] == "upbit"

def test_update_api_key_status(client: TestClient, db):
    """API 키 상태 업데이트 테스트"""
    # 먼저 API 키 생성
    create_response = client.post(
        "/api/v1/api-keys/",
        json={
            "exchange": "upbit",
            "access_key": "test-access-key",
            "secret_key": "test-secret-key"
        }
    )
    key_id = create_response.json()["id"]
    
    # API 키 상태 업데이트
    response = client.put(
        f"/api/v1/api-keys/{key_id}/status",
        json={"is_active": False}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "API 키 상태가 업데이트되었습니다."
    
    # 상태 변경 확인
    get_response = client.get(f"/api/v1/api-keys/{key_id}")
    assert get_response.json()["is_active"] is False

def test_delete_api_key(client: TestClient, db):
    """API 키 삭제 테스트"""
    # 먼저 API 키 생성
    create_response = client.post(
        "/api/v1/api-keys/",
        json={
            "exchange": "upbit",
            "access_key": "test-access-key",
            "secret_key": "test-secret-key"
        }
    )
    key_id = create_response.json()["id"]
    
    # API 키 삭제
    response = client.delete(f"/api/v1/api-keys/{key_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "API 키가 삭제되었습니다."
    
    # 삭제 확인
    get_response = client.get(f"/api/v1/api-keys/{key_id}")
    assert get_response.status_code == 404

def test_get_nonexistent_api_key(client: TestClient, db):
    """존재하지 않는 API 키 조회 테스트"""
    response = client.get("/api/v1/api-keys/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "API 키를 찾을 수 없습니다." 