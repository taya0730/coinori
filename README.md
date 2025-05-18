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

```

## 환경 변수 설정

### 백엔드 환경 변수 예제 (`backend/.env.example`)
- DATABASE_URL: 데이터베이스 접속 주소
- SECRET_KEY: JWT 및 보안용 시크릿 키
- ALGORITHM: JWT 알고리즘
- ACCESS_TOKEN_EXPIRE_MINUTES: 토큰 만료 시간(분)
- BACKEND_CORS_ORIGINS: 허용할 CORS 오리진
- BINANCE_API_URL, UPBIT_API_URL: 거래소 API 주소
- DEFAULT_TRADE_AMOUNT, MAX_TRADE_AMOUNT, DEFAULT_STOP_LOSS, DEFAULT_TAKE_PROFIT: 트레이딩 기본값

### 프론트엔드 환경 변수 예제 (`frontend/.env.example`)
- REACT_APP_API_URL: 백엔드 API 서버 주소

환경 변수 파일을 실제로 사용하려면 아래와 같이 복사해서 사용하세요:

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

## 개발 환경 설정

### 필수 요구사항
- Docker
- Docker Compose
- Git

### 프로젝트 설정 방법

1. GitHub 저장소 클론
```bash
git clone https://github.com/[your-username]/coinori.git
cd coinori
```

2. 환경 변수 설정
```bash
# backend/.env 파일 생성
cp backend/.env.example backend/.env

# frontend/.env 파일 생성
cp frontend/.env.example frontend/.env
```

3. Docker 컨테이너 실행
```bash
# 컨테이너 빌드 및 실행
docker-compose up --build

# 백그라운드에서 실행하려면
docker-compose up -d --build
```

4. 서비스 접속
- Backend API: http://localhost:8000
- Frontend: http://localhost:3000
- Database: localhost:5432

### 개발 가이드

1. Git 브랜치 전략
- main: 프로덕션 브랜치
- develop: 개발 브랜치
- feature/*: 기능 개발 브랜치
- hotfix/*: 긴급 수정 브랜치

2. 커밋 메시지 규칙
- feat: 새로운 기능
- fix: 버그 수정
- docs: 문서 수정
- style: 코드 포맷팅
- refactor: 코드 리팩토링
- test: 테스트 코드
- chore: 빌드 업무 수정

3. 코드 리뷰
- PR 생성 전 self-review 진행
- 코드 컨벤션 준수
- 테스트 코드 작성
- 문서화

## 라이선스
MIT License
