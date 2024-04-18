from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_search_for_the_add_to_cart_button(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_element(
        By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")

    assert button, f"The site page does not contain a button: 'Add to cart'"
    print("Кнопка называется: ", button.text)
