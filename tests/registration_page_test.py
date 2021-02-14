import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from time import sleep

# DANE TESTOWE
valid_name = "Marcin"
valid_surname = "Nowak"
valid_gender = "female"
valid_country_code = "+48"
valid_phone_number = "123123123"
valid_email = "kljkjdk@poczta.onet.pl"
valid_password = "Qwerty1231"
valid_nationality = "Polska"

invalid_email = "ljkdfdf.pl"


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
        rp.fill_name(valid_name)
        # Wpisz nazwisko
        rp.fill_surname(valid_surname)
        # Wybierz płeć
        rp.choose_gender(valid_gender)
        # Wpisz kod kraju
        rp.fill_country_code(valid_country_code)
        # Wpisz numer telefonu
        rp.fill_telephone_number(valid_phone_number)
        # Wpisz NIEPOPRAWNY E-MAIL
        rp.fill_email(invalid_email)
        # Wpisz hasło
        rp.fill_password(valid_password)
        # Wybierz nardowość
        rp.choose_nationality(valid_nationality)



        # FAKTYCZNY TEST - SPRAWDZANIE OCZEKIWANEGO REZULTATU
        # rp.verify_visible_errors(1, ["Nieprawidłowy adres e-mail"])
        # rp.verify_visible_errors(2, ["Należy używać tylko liter alfabetu łacińskiego, bez znaków diakrytycznych (np.: á, é, ő) i unikać używania znaków specjalnych!",
        #                              "Niepraidłowy adrtes e-mail"])


        sleep(3)

if __name__=="__main__":
    unittest.main(verbosity=2)