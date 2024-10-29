import re

def prepreprocess_text():
  pass

def get_ocr_result(content, ocr_texts: list, ocr_unique_texts: set, ocr_model):
    ocr_results = []
      
    ocr_results = ocr_model.ocr(content)
    print(f'ocr_en_results: {ocr_results}')

    for ocr_result in ocr_results[0]:
        ocr_text = ocr_result[1][0]
        # print(f'ocr_en_result: {ocr_en_text}')
        if ocr_text not in ocr_unique_texts:
            ocr_texts.append(ocr_text)
            ocr_unique_texts.add(ocr_text)

    print(f'ocr_texts: {ocr_texts}')

def postpreprocess_text(ocr_texts: list, ocr_unique_texts: set):

    kr_en_pattern = r'^[가-힣a-zA-Z]+$'
    parsed_ocr_set = set()

    for text in ocr_texts:
        # 단위 제외
        if text in ['mg', 'g', 'ml', 'l']: continue

        elif re.match(kr_en_pattern, text):
           parsed_ocr_set.add(text)

    return parsed_ocr_set