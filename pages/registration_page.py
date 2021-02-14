from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import RegistrationPageLocators

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

    # Podanie kodu kraju
    def choose_country_code(self, country_code):
        pass

    # Wpisanie kodu kraju
    def fill_country_code(self, country_code):
        self.driver.find_element(*RegistrationPageLocators.COUNTRY_CODE_DIV).click()
        self.driver.find_element(*RegistrationPageLocators.COUNTRY_CODE_INPUT).send_keys(country_code, Keys.RETURN)

    # Wpisanie nru telefonu
    def fill_telephone_number(self, phone_number):
        self.driver.find_element(*RegistrationPageLocators.TELEPHONE_NUMBER_INPUT).send_keys(phone_number)

    # Wpisanie e-maila
    def fill_email(self, wpisywany_email):
        self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(wpisywany_email)

    # Wpisanie hasła
    def fill_password(self, password):
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)

    def choose_nationality(self, nationality):
        # Kliknięcie w input, żeby rozwinąć kraje
        self.driver.find_element(*RegistrationPageLocators.NATIONALITY_INPUT).click()
        # driver.find_element_by_xpath('//input[@data-test="booking-register-country"]').click()
        # Wyszukanie konteneru z krajami
        countries_labels = self.driver.find_elements(*RegistrationPageLocators.COUNTRY_LABELS)
        for label in countries_labels:
            # Szukaj wewnątrz elementu label
            country = label.find_element_by_tag_name('strong')
            # Pobierz i wypisz wewnętrzny tekst elementu country
            # print(country.get_attribute("innerText"))
            if country.get_attribute("innerText") == nationality:
                # Przewiń do wybranego kraju
                country.location_once_scrolled_into_view
                # To w niego kliknij
                country.click()
                # ... i nie szukaj dalej
                break

    # # Wybór narodowości (ZŁE (BAD!!!) NIE DO UŻYTKU))
    # def choose_nationality_bad(self, nationality):
    #     # 10. Wybierz narodowość
    #     # Kliknięcie w input, żeby rozwinąć kraje
    #
    #     # Wyszukanie konteneru z krajami
    #     countries_container = driver.find_element_by_class_name('register-form__country-container__locations')
    #     # Szukam WEWNĄTRZ konteneru z krajami labelek
    #     # Metoda zwróci LISTĘ WebElementów [WebElement, WebElement, Webelement....]
    #     countries_list = countries_container.find_elements_by_tag_name('label')
    #     print("Liczba krajów", len(countries_list))
    #     # Powtarzaj dla każdego elementu w liście krajów
    #     for label in countries_list:
    #         # Szukaj wewnątrz elementu label
    #         country = label.find_element_by_tag_name('strong')
    #         # Pobierz i wypisz wewnętrzny tekst elementu country
    #         # print(country.get_attribute("innerText"))
    #         if country.get_attribute("innerText") == chosen_country:
    #             # Przewiń do wybranego kraju
    #             country.location_once_scrolled_into_view
    #             # To w niego kliknij
    #             country.click()
    #             # ... i nie szukaj dalej
    #             break


    # Sprawdzenie widocznych błędów
    def verify_visible_errors(self, number_of_errors, errors_text):
        # number_of_errors - liczba widocznych błędów
        # errors_text - lista z treściami błędów
        # np. verify_visible_errors(1, ["Nieprawidłowy e-mail"])
        # np. verify_visible_errors(2, ["Wybierz płeć", "Podaj hasło"])
        # PSEUDOKOD:
        # Wyszukaj iformacje o błędach (lista)
        # Stwórz pustą listę widocznych błędów
        # Dla kazdego błędu w liście informacji o błędach (for..)
        # Jeśli błąd jest widoczny
        # Dodaj do listy widocznych błędów
        # Sprawdź, czy liczna widocznych błędów jest właściwa
        # Stwórz (pustą) listę zawierającą (teksty) informacji o błędach
        # Przez tyle razy, ile jest widocznych błędów (for..)
        # Dodaj tekst błędu do listy informacji o błędach
        # Porównaj obie listy z tekstami błędów: zadaną oraz faktyczną
