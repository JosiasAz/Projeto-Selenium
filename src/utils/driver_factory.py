from __future__ import annotations
from pathlib import Path
from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .paths import project_root
from src.config.settings import DOWNLOAD_DIR, HEADLESS

def create_chrome(download_dir: Optional[str] = None):
    download_dir = download_dir or DOWNLOAD_DIR
    abs_download = (project_root() / download_dir).resolve()
    abs_download.mkdir(parents=True, exist_ok=True)

    options = Options()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,768")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("prefs", {
        "download.default_directory": str(abs_download),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
