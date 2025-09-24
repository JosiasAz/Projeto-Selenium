import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis do .env na raiz do projeto
ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
LOGIN_URL = os.getenv("LOGIN_URL", f"{BASE_URL}/login")
USER_EMAIL = os.getenv("USER_EMAIL", "tomsmith")
USER_PASSWORD = os.getenv("USER_PASSWORD", "SuperSecretPassword!")
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "downloads")
HEADLESS = os.getenv("HEADLESS", "true").lower() in ("1", "true", "yes")
TESSERACT_PATH = os.getenv("TESSERACT_PATH", "")
