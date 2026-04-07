# backend/ingestion/ocr.py

from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_text(image_path):
    result = ocr.ocr(image_path)
    text = " ".join([line[1][0] for line in result[0]])
    return text