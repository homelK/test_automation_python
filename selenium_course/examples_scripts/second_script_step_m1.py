import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"
# link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # link1 = browser.find_element(By.PARTIAL_LINK_TEXT, link_text)
    # link1.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Gervasi")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Vylivaha")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Ragachou")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Belarus")
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


