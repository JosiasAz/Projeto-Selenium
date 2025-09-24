import sys
from pathlib import Path

# conftest.py está em: src/tests/conftest.py
# parents[0] = tests, [1] = src, [2] = raiz do projeto
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
# --- fim: ajuste de sys.path ---

import os
import pytest
from datetime import datetime
from src.utils.driver_factory import create_chrome
from src.config import settings

@pytest.fixture(scope="session")
def base_url():
    return settings.BASE_URL

@pytest.fixture
def driver():
    driver = create_chrome()
    yield driver
    driver.quit()
    
def pytest_exception_interact(node, call, report):
    if report.failed and hasattr(node, 'funcargs') and 'driver' in node.funcargs:
        from datetime import datetime
        import os
        driver = node.funcargs['driver']
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)
        png = os.path.join(reports_dir, f"screenshot-{ts}.png")
        html = os.path.join(reports_dir, f"page-{ts}.html")
        try:
            driver.save_screenshot(png)
            with open(html, "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            print(f"\n[pytest] Artefatos salvos: {png}  {html}")
        except Exception as e:
            print(f"\n[pytest] Falha ao salvar artefatos: {e}")


def pytest_exception_interact(node, call, report):
    # Tira screenshot quando ocorrer falha
    if report.failed and hasattr(node, 'funcargs') and 'driver' in node.funcargs:
        driver = node.funcargs['driver']
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)
        path = os.path.join(reports_dir, f"screenshot-{ts}.png")
        try:
            driver.save_screenshot(path)
            print(f"\n[pytest] Screenshot salvo em: {path}")
        except Exception as e:
            print(f"\n[pytest] Falha ao salvar screenshot: {e}")
