from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.wait_utils import wait_visible

class SecurePage(BasePage):
    HEADER = (By.TAG_NAME, "h2")  # 'Secure Area'
    CONTENT = (By.ID, "content")

    def header_text(self) -> str:
        return wait_visible(self.driver, self.HEADER).text
