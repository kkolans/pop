from pages.base_page import BasePage
from locators import RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):
    """
    Strona rejestracji
    """
    def _verify_page(self):
        print("Weryfikacja RegistartionPage")
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
        # Wyszukać input nazwiska
        element = self.driver.find_element(*RegistrationPageLocators.SURNAME_INPUT)
        # Wpisać w ten input to nazwisko (surname)
        element.send_keys(surname)

    # Wybór płci
    def choose_gender(self, gender):
        if gender == "female":
            # Kliknij Nazwisko, aby odsłonić
            self.driver.find_element(*RegistrationPageLocators.SURNAME_INPUT).click()
            # Wybierz kobietę
            self.driver.find_element(*RegistrationPageLocators.GENDER_FEMALE_BTN).click()
        else:
            # Kliknij Imię, aby odsłonić
            self.driver.find_element(*RegistrationPageLocators.NAME_INPUT).click()
            # Wybierz mężczyżnę
            self.driver.find_element(*RegistrationPageLocators.GENDER_MALE_BTN).click()


    def choose_gender(self, gender):
        if gender == "female":
            # Kliknij Nazwisko, aby odsłonić
            self.driver.find_element(*RegistrationPageLocators.SURNAME_INPUT).click()
            # Wybierz kobietę
            self.driver.find_element(*RegistrationPageLocators.GENDER_FEMALE_BTN).click()
        else:
            # Kliknij Imię, aby odsłonić
            self.driver.find_element(*RegistrationPageLocators.NAME_INPUT).click()
            # Wybierz mężczyżnę
            self.driver.find_element(*RegistrationPageLocators.GENDER_MALE_BTN).click()


    # Podanie kodu kraju
    # Wpisanie nru telefonu
    # Wpisanie e-maila
    # Wpisanie hasła
    # Wybór narodowości
