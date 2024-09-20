import time
from selenium.webdriver.common.by import By

def test_add_to_basket_btn_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(30)
    assert browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]").is_displayed(), "The button 'add to basket' is not found"