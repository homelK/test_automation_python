from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    invitation_btn = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    invitation_btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    elm_with_expression = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_value = elm_with_expression.text

    math_exp_value = calc(x_value)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(math_exp_value)

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
