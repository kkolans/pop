from pages.base_page import BasePage
from locators import HomePageLocators

class HomePage(BasePage):
    """
    Strona domowa
    """

    def click_zaloguj_btn(self):
        element = self.driver.find_element(*HomePageLocators.ZALOGUJ_BTN)
        element.click()
