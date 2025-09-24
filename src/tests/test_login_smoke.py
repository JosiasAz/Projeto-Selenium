import pytest
from src.pages.login_page import LoginPage
from src.pages.secure_page import SecurePage
from src.config.settings import USER_EMAIL, USER_PASSWORD

@pytest.mark.smoke
def test_login_sucesso(driver):
    lp = LoginPage(driver)
    lp.open_login()
    lp.login(USER_EMAIL, USER_PASSWORD)
    sp = SecurePage(driver)
    assert "Secure Area" in sp.header_text()
