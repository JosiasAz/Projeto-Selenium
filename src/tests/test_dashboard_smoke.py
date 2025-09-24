import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.config.settings import USER_EMAIL, USER_PASSWORD, BASE_URL

@pytest.mark.smoke
def test_dashboard_basico(driver):
    # 1) loga
    lp = LoginPage(driver)
    lp.open(BASE_URL + "/login")  # ajuste se necessário
    lp.login(USER_EMAIL, USER_PASSWORD)

    # 2) navega para o dashboard (ajuste a URL ou clique)
    driver.get(BASE_URL + "/secure")  # no demo; no seu sistema: /dashboard

    # 3) valida elementos do dashboard
    db = DashboardPage(driver)
    assert db.title_text(), "Título do dashboard não encontrado"
