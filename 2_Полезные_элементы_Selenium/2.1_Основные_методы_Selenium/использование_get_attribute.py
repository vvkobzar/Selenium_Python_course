import time
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://suninjuly.github.io/get_attribute.html")

try:

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = driver.find_element(By.XPATH, "//img[@id='treasure']")
    x_attribute = x_element.get_attribute("valuex")
    x = x_attribute
    y = calc(x)

    driver.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
    driver.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    driver.find_element(By.XPATH, "//input[@id='robotsRule']").click()

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

finally:

    time.sleep(15)

    driver.quit()
