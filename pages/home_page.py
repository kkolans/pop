from pages.base_page import BasePage
from locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    """
    Strona domowa
    """
    def click_zaloguj_btn(self):
        # Tworzenie instancji klasy WebDriverWait
        wait = WebDriverWait(self.driver, 60)
        # Wywołanie metody until na obiekcie WebDriverWait
        # W efekcie otrzymamy element (jeśli warunek wystąpi)
        element = wait.until(EC.element_to_be_clickable(*HomePageLocators.ZALOGUJ_BTN))
        # element = self.driver.find_element(*HomePageLocators.ZALOGUJ_BTN)
        element.click()

    def _verify_page(self):
        assert "Oficjalna strona Wizz Air" in self.driver.title

