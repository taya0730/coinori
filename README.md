# Coinori - 암호화폐 자동 트레이딩 서비스

## 주의사항
1. 작업 중인 소스 코드를 임의로 건드리지 않습니다.
2. 파일 생성이나 실행 전에 반드시 허가를 받아야 합니다.
3. 프로젝트는 모두 Docker로 실행합니다.

## 프로젝트 구조
```
coinori/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── trading/
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
