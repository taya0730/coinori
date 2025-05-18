from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.api import api_router

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# API 라우터 등록
app.include_router(api_router, prefix=settings.API_V1_STR)




