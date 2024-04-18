import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

chrome = Service(executable_path=ChromeDriverManager().install())
firefox = Service(executable_path=GeckoDriverManager().install())


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Select a language using the command: --language= ")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(service=chrome, options=options)

    elif browser_name == 'firefox':
        if user_language != None:
            print("\nstart firefox browser for test..")
            options = FirefoxOptions()
            options.set_preference("intl.accept_languages", user_language)
            driver = webdriver.Firefox(service=firefox, options=options)
        else:
            driver = webdriver.Firefox(service=firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()
