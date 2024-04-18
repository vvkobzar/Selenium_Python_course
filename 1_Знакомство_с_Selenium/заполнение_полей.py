import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

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
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

time.sleep(10)


driver.quit()
