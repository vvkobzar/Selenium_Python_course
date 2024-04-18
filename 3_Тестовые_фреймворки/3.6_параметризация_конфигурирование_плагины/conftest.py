import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

chrome = Service(executable_path=ChromeDriverManager().install())
firefox = Service(executable_path=GeckoDriverManager().install())


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(service=chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox(service=firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()
