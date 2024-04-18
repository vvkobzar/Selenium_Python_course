import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


class TestRegistration(unittest.TestCase):
    def test_test_1(self):
        driver.get("http://suninjuly.github.io/registration1.html")

        driver.find_element(
            By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Ivan")
        driver.find_element(
            By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Petrov")
        driver.find_element(
            By.XPATH, "//input[@placeholder='Input your email']").send_keys("email@gmail.com")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(1)

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        actual_result = welcome_text_elt.text
        expected_result = "Congratulations! You have successfully registered!"

        self.assertEqual(expected_result, actual_result,
                         f"expected {expected_result}, got {actual_result}")

    def test_test_2(self):
        driver.get("http://suninjuly.github.io/registration2.html")

        driver.find_element(
            By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Ivan")
        driver.find_element(
            By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Petrov")
        driver.find_element(
            By.XPATH, "//input[@placeholder='Input your email']").send_keys("email@gmail.com")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(1)

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        actual_result = welcome_text_elt.text
        expected_result = "Congratulations! You have successfully registered!"

        self.assertEqual(expected_result, actual_result,
                         f"expected {expected_result}, got {actual_result}")


if __name__ == "__main__":
    unittest.main()
