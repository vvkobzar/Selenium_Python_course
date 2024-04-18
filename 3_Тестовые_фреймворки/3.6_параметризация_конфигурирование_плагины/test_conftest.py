from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(driver):
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "#login_link")
