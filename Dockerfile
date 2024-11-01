FROM python:3.10.15

WORKDIR /app

# 추가 lib 설치
RUN apt-get update && apt-get install --no-install-recommends -y \
    pkg-config \
    python3-dev \ 
    default-libmysqlclient-dev \
    build-essential \ 
    libegl1 \
    libgl1 \
    libgomp1 \
    libglib2.0-0 \
    python3-pip

# requirements.txt만 먼저 복사하여 의존성을 캐시
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 파일을 복사
COPY . .

EXPOSE 8081

RUN ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]