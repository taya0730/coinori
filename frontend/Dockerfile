FROM node:18-alpine

WORKDIR /app

# 패키지 파일 복사 및 설치
COPY package*.json ./
RUN npm install

# 소스 코드 복사
COPY . .

# 포트 설정
EXPOSE 3000

# 개발 서버 실행
CMD ["npm", "start"]

RUN apt-get update && apt-get install -y git




