from pages.base_page import BasePage
from locators import RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):
    """
    Strona rejestracji
    """
    def _verify_page(self):
        # Tutaj będziemy weryfikować stronę
        wait = WebDriverWait(self.driver, 60)
        # Wywołanie metody until na obiekcie WebDriverWait
        # W efekcie otrzymamy element (jeśli warunek wystąpi)
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))


    # Wpisanie imienia
    def fill_name(self, name):
        # Wyszukac input imienia
        element = self.driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        # Wpisac w ten input to imię (name)
        element.send_keys(name)

    # Wpisanie nazwiska
    def fill_surname(self, surname):
        # Do zaimplementowania
        pass

    # Wybór płci
    def choose_gender(self, gender):
        # Do zaimplementowania
        pass

    # Podanie kodu kraju
    # Wpisanie nru telefonu
    # Wpisanie e-maila
    # Wpisanie hasła
    # Wybór narodowości
