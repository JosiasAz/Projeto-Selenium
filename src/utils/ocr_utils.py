from typing import Optional
import pytesseract
from PIL import Image
from src.config.settings import TESSERACT_PATH

if TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def read_text_from_image(image_path: str, lang: str = "eng") -> Optional[str]:
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=lang)
        return text.strip()
    except Exception as e:
        return None
