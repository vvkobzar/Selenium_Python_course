import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://suninjuly.github.io/selects1.html")

try:
    num_1 = driver.find_element(By.XPATH, "//span[@id='num1']")
    num_2 = driver.find_element(By.XPATH, "//span[@id='num2']")
    sum_num = str(int(num_1.text) + int(num_2.text))

    select = Select(driver.find_element(By.XPATH, "//select[@id='dropdown']"))
    select.select_by_value(sum_num)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

finally:

    time.sleep(15)

    driver.quit()
