import os
import time
import pytest
from selenium.webdriver.common.by import By
from src.utils.wait_utils import wait_clickable, wait_visible
from src.config.settings import BASE_URL
from src.utils.paths import project_root

@pytest.mark.e2e
def test_download_arquivo(driver):
    # Página de downloads demo
    driver.get(f"{BASE_URL}/download")
    link = wait_clickable(driver, (By.LINK_TEXT, "some-file.txt"))
    link.click()

    # Verifica arquivo na pasta de downloads
    downloads = project_root() / "downloads"
    for _ in range(20):
        files = list(downloads.glob("*.txt"))
        if files:
            assert any(f.name.startswith("some-file") for f in files)
            return
        time.sleep(0.5)
    pytest.fail("Arquivo não foi baixado em tempo hábil")
