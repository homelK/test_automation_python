import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

current_dir = os.path.abspath(os.path.dirname(__file__))

path_to_file = os.path.join(current_dir, "test.txt")

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
    first_name.send_keys("First name")

    last_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]")
    last_name.send_keys("Last name")

    email = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
    email.send_keys("email@com.by")

    add_file_btn = browser.find_element(By.ID, "file")
    add_file_btn.send_keys(path_to_file)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()