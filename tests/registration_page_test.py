import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from time import sleep

name = "Marcin"
surname = "Nowak"
gender = "female"
country_code = "+48"
phone_number = "123123123"

class RegistrationPageTest(BaseTest):
    """
    Test strony Rejestracji
    """
    def setUp(self):
        print("setUp z RegistrationPageTest")
        # Wywołanie metody setUp z klasy nadrzędnej (BaseTest)
        super().setUp()
        # Kliknięcie zaloguj
        # Stworzenie instancji klasy HomePage (hp)
        hp = HomePage(self.driver)
        # Użycie metody click_zaloguj_btn zawartej w obiekcie hp klasy HomePage
        hp.click_zaloguj_btn()
        # Kliknięcie Rejestracja na stronie Logowania
        # Stworzenie instancji klasy LoginPage (lp)
        lp = LoginPage(self.driver)
        # Użycie metody click_register_btn zawartej w obiekcie lp klasy LoginPage
        lp.click_register_btn()

    def test_incorrect_email(self):
        # Stworzenie instancji klasy RegistrationPage (rp)
        rp = RegistrationPage(self.driver)
        # Wpisz imię
        rp.fill_name(name)
        # Wpisz nazwisko
        rp.fill_surname(surname)
        # Wybierz płeć
        rp.choose_gender(gender)
        # Wpisz kod kraju
        rp.fill_country_code(country_code)
        # Wpisz numer telefonu
        rp.fill_telephone_number(phone_number)


        # FAKTYCZNY TEST - SPRAWDZANIE OCZEKIWANEGO REZULTATU
        # rp.verify_visible_errors(1, ["Nieprawidłowy adres e-mail"])
        # rp.verify_visible_errors(2, ["Należy używać tylko liter alfabetu łacińskiego, bez znaków diakrytycznych (np.: á, é, ő) i unikać używania znaków specjalnych!",
        #                              "Niepraidłowy adrtes e-mail"])


        sleep(3)

if __name__=="__main__":
    unittest.main(verbosity=2)