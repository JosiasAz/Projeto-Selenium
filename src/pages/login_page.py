from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.wait_utils import wait_visible, wait_clickable
from src.config.settings import LOGIN_URL

class LoginPage(BasePage):
    USER = (By.ID, "username")
    PASS = (By.ID, "password")
    BTN_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def open_login(self):
        self.open(LOGIN_URL)

    def login(self, username: str, password: str):
        wait_visible(self.driver, self.USER).send_keys(username)
        wait_visible(self.driver, self.PASS).send_keys(password)
        wait_clickable(self.driver, self.BTN_LOGIN).click()

    def get_flash_message(self) -> str:
        return wait_visible(self.driver, self.FLASH).text
