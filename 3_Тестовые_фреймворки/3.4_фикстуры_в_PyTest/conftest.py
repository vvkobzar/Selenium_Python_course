import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def driver():
    print("\nstart driver for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit driver..")
    driver.quit()
