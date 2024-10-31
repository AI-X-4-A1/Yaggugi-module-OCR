from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from utils import *

import os

os.environ['KMP_DUPLICATE_LIB_OK']='True' #이거 안해주면 오류남

# Setup model
ocr_en_model = PaddleOCR(lang='en')
ocr_kr_model = PaddleOCR(lang='korean')

app = FastAPI()

@app.post("/ocr/")
async def create_upload_files(file: UploadFile):
    content = await file.read()

    ocr_texts = []              # 순서 유지
    ocr_unique_texts = set()    # 중복 체크

    # preprocess
    content = prepreprocess_text(content)

    # ocr
    get_ocr_result(content, ocr_texts, ocr_unique_texts, ocr_en_model)  # en
    get_ocr_result(content, ocr_texts, ocr_unique_texts, ocr_kr_model)  # ko

    # postpreprocess
    ocr_pp_unique_text = postpreprocess_text(ocr_texts, ocr_unique_texts)
    print(f'ocr_pp_unique_text: {ocr_pp_unique_text}')

    return {"ocr_result": ocr_pp_unique_text}
