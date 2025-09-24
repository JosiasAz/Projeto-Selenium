from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.wait_utils import wait_visible

class DashboardPage(BasePage):
    TITLE = (By.TAG_NAME, "h1")           
    KPI_CARD = (By.CSS_SELECTOR, ".kpi") 

    def title_text(self):
        return wait_visible(self.driver, self.TITLE).text

    def has_kpis(self):
        return len(self.driver.find_elements(*self.KPI_CARD)) > 0
