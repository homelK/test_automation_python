from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price_text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    elm_with_expression = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_value = elm_with_expression.text

    math_exp_value = calc(x_value)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(math_exp_value)

    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()


finally:
    time.sleep(10)
    browser.quit()