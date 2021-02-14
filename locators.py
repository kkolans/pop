from selenium.webdriver.common.by import By

class HomePageLocators():
    """
    Lokatory strony głównej
    """
    ZALOGUJ_BTN = (By.XPATH, '//button[@data-test="navigation-menu-signin"]')

class LoginPageLocators():
    """
    Lokatory strony logowania
    """
    REGISTER_BTN = (By.XPATH, '//button[@data-test="registration"]')

class RegistrationPageLocators():
    """
    Lokatory strony rejestracji
    """
    NAME_INPUT = (By.NAME, 'firstName')
    SURNAME_INPUT = (By.NAME, 'lastName')