from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from utils import *
from fileinput import close

import os
import cv2

os.environ['KMP_DUPLICATE_LIB_OK']='True' #이거 안해주면 오류남

# Setup model
ocr_en_model = PaddleOCR(lang='en')
ocr_kr_model = PaddleOCR(lang='korean')

app = FastAPI()

@app.post("/ocr")
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

from fileinput import close
import cv2

@app.get("/capture")
async def capture_web_cam():
  capture = cv2.VideoCapture(0)  # 0번 카메라 연결

  if capture.isOpened() == False:
    print("camera open failed")
    exit()

  isCapture = True
  img = None
  def mouse_handler_result(event, x, y, flag, param):
    nonlocal img
    nonlocal isCapture
    if event == cv2.EVENT_LBUTTONDOWN:
      img = param
      isCapture = False
      cv2.destroyAllWindows()
    if event == cv2.EVENT_RBUTTONDOWN:
      cv2.destroyWindow("result")

  def mouse_handler_capture(event, x, y, flag, param):
    nonlocal isCapture
    if event == cv2.EVENT_LBUTTONDOWN:
      result_frame = frame
      cv2.imshow("result", result_frame)
      cv2.setMouseCallback("result", mouse_handler_result, param = result_frame)
    if event == cv2.EVENT_RBUTTONDOWN:
      cv2.destroyWindow("capture")
      isCapture = False

  while isCapture:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기

    if not ret:
      print("Can't read camera")
      break

    cv2.namedWindow("capture")
    cv2.setMouseCallback("capture", mouse_handler_capture)
    
    cv2.imshow("capture", frame)

    if cv2.waitKey(1) == 27:
      isCapture = False

  capture.release()
  res, img_jpg = cv2.imencode(".jpg", img)
  return StreamingResponse(io.BytesIO(img_jpg.tobytes()), media_type = "image/jpg")