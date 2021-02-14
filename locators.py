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
    GENDER_FEMALE_BTN = (By.XPATH, '//label[@data-test="register-genderfemale"]')
    GENDER_MALE_BTN = (By.XPATH, '//label[@data-test="register-gendermale"]')
    COUNTRY_CODE_DIV = (By.XPATH, '//div[@data-test="booking-register-country-code"]')
    COUNTRY_CODE_INPUT = (By.NAME, 'phone-number-country-code')
    TELEPHONE_NUMBER_INPUT = (By.NAME, 'phoneNumberValidDigits')
    EMAIL_INPUT = (By.NAME, 'email')
    # EMAIL_INPUT = (By.XPATH, '//input[@data-test="booking-register-email"]')
    PASSWORD_INPUT = (By.NAME, 'password')
    NATIONALITY_INPUT = (By.XPATH, '//input[@data-test="booking-register-country"]')
    COUNTRY_CONTAINER_DIV = (By.CLASS_NAME, 'register-form__country-container__locations')
    COUNTRY_LABELS = (By.XPATH, '//div[@class="register-form__country-container__locations"]/label')