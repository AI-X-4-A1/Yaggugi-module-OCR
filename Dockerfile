FROM python:3.10.15

WORKDIR /app

# requirements.txt만 먼저 복사하여 의존성을 캐시
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 파일을 복사
COPY . .