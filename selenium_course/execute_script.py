from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    elm_with_expression = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_value = elm_with_expression.text

    math_exp_value = calc(x_value)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(math_exp_value)

    browser.execute_script("window.scrollBy(0, 100);")

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio_btn_rbot = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_btn_rbot.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")

    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
