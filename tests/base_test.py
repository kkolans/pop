import unittest
from selenium import webdriver

# Klasa BaseTest dziedziczy po klasie TestCase
class BaseTest(unittest.TestCase):
    """
    Klasa bazowa każdego testu
    """
    def setUp(self):
        print("Setup z BaseTest")
        self.driver = webdriver.Chrome()
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.maximize_window()

    def tearDown(self):
        print("tearDown z BaseTest")
        self.driver.quit()
