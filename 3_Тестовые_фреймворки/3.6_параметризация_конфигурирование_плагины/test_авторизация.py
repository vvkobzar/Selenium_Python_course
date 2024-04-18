import os
import math
import time
import pytest

from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()  # Нужно создать .env
login = os.environ.get("DB_LOGIN")
password = os.environ.get("DB_PASSWORD")


def calk():
    return str(math.log(int(time.time())))


@pytest.mark.parametrize('pages', ['895', '896', '897', '898', '899', '903', '904', '905'])
def test_authorization_on_stepik(driver, pages):
    link = f"https://stepik.org/lesson/236{pages}/step/1"
    driver.get(link)
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='ember420']"))).click()
    driver.switch_to.active_element

    driver.find_element(
        By.XPATH, "//input[@name='login']").send_keys(login)
    driver.find_element(
        By.XPATH, "//input[@name='password']").send_keys(password)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    driver.implicitly_wait(10)

    assert driver.find_element(
        By.XPATH, "//button[@aria-label='Profile']"), f"You are not logged in to your account"

    driver.find_element(
        By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']").send_keys(calk())
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH, "//button[@class='submit-submission']"))).click()

    optional_feedback = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//p[@class='smart-hints__hint']")))
    assert optional_feedback.text == 'Correct!', f"The optional feedback: {optional_feedback.text} does not match the line 'Correct!'"
