# 🚀 Coinori - Bitcoin Automated Trading Service

> 비트코인 자동 거래 서비스 프로젝트입니다.

## 🛠 기술 스택

| 구분 | 기술 |
|:---:|:---|
| Backend | Python (FastAPI) |
| Frontend | React |
| Database | PostgreSQL |
| Container | Docker |
| CI/CD | GitHub Actions |
| Code Quality | SonarQube |

## 📁 환경 구축 내용

### 1. 프로젝트 구조
```
coinori/
├── backend/           # FastAPI 백엔드
├── frontend/          # React 프론트엔드
├── .github/           # GitHub Actions 워크플로우
├── docker-compose.yml # Docker 서비스 설정
└── sonar-project.properties # SonarQube 설정
```

### 2. Docker 환경
- **Backend**: Python 3.11 기반
- **Frontend**: Node.js 18 기반
- **Database**: PostgreSQL 15
- **SonarQube**: 최신 버전

### 3. SonarQube 설정
- 코드 품질 분석 도구 통합
- GitHub Actions를 통한 자동 분석
- `release` 브랜치를 기준 브랜치로 설정

### 4. 개발 환경 설정
- **Backend**
  - FastAPI 프레임워크
  - PostgreSQL 데이터베이스 연동
  - 환경 변수 설정 (.env)

- **Frontend**
  - React 18
  - Material-UI
  - 환경 변수 설정 (.env)

### 5. 브랜치 전략
- `main`: 개발 브랜치
- `release`: 배포 브랜치 (SonarQube 기준 브랜치)

---

## 🚀 실행 방법

### 1. 환경 변수 설정
```bash
# Backend (.env)
DATABASE_URL=postgresql://postgres:postgres@db:5432/coinori
SECRET_KEY=your-secret-key-here

# Frontend (.env)
REACT_APP_API_URL=http://localhost:8000
```

### 2. Docker 실행
```bash
# 모든 서비스 실행
docker-compose up -d

# 개별 서비스 재시작
docker-compose restart [service_name]
```

### 3. 서비스 접속
| 서비스 | URL |
|:---:|:---|
| Backend API | http://localhost:8000 |
| Frontend | http://localhost:3000 |
| SonarQube | http://localhost:9000 |
| Database | localhost:5432 |

---

## 📊 코드 품질 관리
- SonarQube를 통한 자동 코드 분석
- GitHub Actions를 통한 CI/CD 파이프라인
- 커밋 시 자동 코드 품질 검사

---

## 📂 프로젝트 구조
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

---

## 🔧 환경 변수 설정

### 백엔드 환경 변수 예제 (`backend/.env.example`)
| 변수 | 설명 |
|:---|:---|
| DATABASE_URL | 데이터베이스 접속 주소 |
| SECRET_KEY | JWT 및 보안용 시크릿 키 |
| ALGORITHM | JWT 알고리즘 |
| ACCESS_TOKEN_EXPIRE_MINUTES | 토큰 만료 시간(분) |
| BACKEND_CORS_ORIGINS | 허용할 CORS 오리진 |
| BINANCE_API_URL | 바이낸스 API 주소 |
| UPBIT_API_URL | 업비트 API 주소 |
| DEFAULT_TRADE_AMOUNT | 기본 거래 금액 |
| MAX_TRADE_AMOUNT | 최대 거래 금액 |
| DEFAULT_STOP_LOSS | 기본 손절 비율 |
| DEFAULT_TAKE_PROFIT | 기본 익절 비율 |

### 프론트엔드 환경 변수 예제 (`frontend/.env.example`)
| 변수 | 설명 |
|:---|:---|
| REACT_APP_API_URL | 백엔드 API 서버 주소 |

환경 변수 파일을 실제로 사용하려면 아래와 같이 복사해서 사용하세요:

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

---

## 💻 개발 환경 설정

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
| 서비스 | URL |
|:---:|:---|
| Backend API | http://localhost:8000 |
| Frontend | http://localhost:3000 |
| Database | localhost:5432 |

---

## 📄 관련 문서
- [기여 가이드라인](CONTRIBUTING.md) - 프로젝트 기여 방법과 주의사항
- [로드맵](ROADMAP.md) - 프로젝트 개발 계획과 진행 상황

## �� 라이선스
MIT License
