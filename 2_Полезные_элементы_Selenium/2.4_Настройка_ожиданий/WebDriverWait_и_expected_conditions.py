import time
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100"))
    driver.find_element(By.XPATH, "//button[@id='book']").click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = driver.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    driver.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
    driver.find_element(By.XPATH, "//button[@id='solve']").click()


finally:
    time.sleep(15)

    driver.quit()
