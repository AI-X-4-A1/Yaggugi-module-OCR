# 약국이 | Yaggugi - OCR
![Python](https://img.shields.io/badge/Python-v3.12.7-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-v2.5.1-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.115.4-009688?style=for-the-badge&logo=fastapi&logoColor=white)


> 약국이는 내 몸에 맞는 영양제를 추천하고, 섭취 일정을 손쉽게 관리하는 맞춤형 건강 앱 입니다.

## 🩺 **Introduction**

+ Paddle OCR 모델을 활용한 영양제 이미지 OCR 서비스 제공

``` bash

<!-- 실행방법 -->
git clone https://github.com/AI-X-4-A1/Yaggugi-module-OCR.git

cd Yaggugi-module-OCR

docker build -t yaggugi-module-ocr .

docker run -d -p 8012:8012 --name yaggugi-module-ocr yaggugi-module-ocr

<!-- 테스트방법 -->

curl -X "POST" \
  "http://127.0.0.1:8012/ocr" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@{{ 이미지 경로 }};type=image/jpeg"

```

## 🩺 **Feature**
+ 영양제 이미지 OCR
  + OCR모델([Paddle OCR](https://github.com/PaddlePaddle/PaddleOCR))

## 🩺 **Folder Structure**

```bash
Yaggugi-module-OCR/
├── main.py               # FastAPI 애플리케이션 코드
├── requirements.txt      # 필요한 패키지 목록
├── paddleocr             # paddle OCR 코드
├── .dockerignore         # Docker 설정 파일 제외 목록
└── Dockerfile            # Docker 설정 파일
```

## 🩺 **Contributor**

- Bigdata92 | 송지섭 | [깃허브](https://github.com/Bigdata92)

## 🩺 **Stack**
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
