import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from time import sleep

name = "Marcin"
surname = "Nowak"

# RegistrationPageTest -> BaseTest -> unittest.TestCase
class RegistrationPageTest(BaseTest):
    """
    Test strony Rejestracji
    """
    def setUp(self):
        print("Metoda setUp z RegistrationPageTest")
        # Wywołanie metody setUp z klasy nadrzędnej (BaseTest)
        super().setUp()
        # # Kliknięcie zaloguj
        # # Stworzenie instancji klasy HomePage (hp)
        # hp = HomePage(self.driver)
        # print(type(hp))
        # # Użycie metody click_zaloguj_btn zawartej w obiekcie hp klasy HomePage
        # hp.click_zaloguj_btn()
        # # Kliknięcie Rejestracja na stronie Logowania
        # # Stworzenie instancji klasy LoginPage (lp)
        # lp = LoginPage(self.driver)
        # # Użycie metody click_register_btn zawartej w obiekcie lp klasy LoginPage
        # lp.click_register_btn()

    def test_incorrect_email(self):
        print("Test Incorrect Email")
        # # Stworzenie instancji klasy RegistrationPage (rp)
        # rp = RegistrationPage(self.driver)
        # # Wpisz imię
        # rp.fill_name(name)
        # # Wpisz nazwisko
        # # .. dalsze kroki

        sleep(3)


if __name__=="__main__":
    unittest.main(verbosity=2)