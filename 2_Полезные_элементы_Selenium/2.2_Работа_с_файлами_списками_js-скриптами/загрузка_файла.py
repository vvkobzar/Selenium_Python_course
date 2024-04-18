import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://suninjuly.github.io/file_input.html")

try:
    driver.find_element(
        By.XPATH, "//input[@name='firstname']").send_keys('Ivan')
    driver.find_element(
        By.XPATH, "//input[@name='lastname']").send_keys('Petrov')
    driver.find_element(
        By.XPATH, "//input[@name='email']").send_keys('email@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(15)

    driver.quit()
