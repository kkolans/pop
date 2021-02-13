import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage

class RegistrationTest(BaseTest):
    """
    Test strony Rejestracji
    """
    def setUp(self):
        # Wywołanie metody setUp z kalsy nadrzędnej (BaseTest)
        super().setUp()
        # Kliknięcie zaloguj
        # Stworzenie instancji klasy HomePage (hp)
        hp = HomePage(self.driver)
        hp.click_zaloguj_btn()
        # Kliknięcie Rejestracja

    def test_incorrect_email(self):
        pass

if __name__=="__main__":
    unittest.main(verbosity=2)