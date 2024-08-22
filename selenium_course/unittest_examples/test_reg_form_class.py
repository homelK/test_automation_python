import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegForm(unittest.TestCase):

    def test_valid_form(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
        first_name.send_keys("First name")

        last_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]")
        last_name.send_keys("Last name")

        email = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
        email.send_keys("email@com.by")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Element text is wrong")
        browser.quit()

    def test_invalid_form(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
        first_name.send_keys("First name")

        last_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]")
        last_name.send_keys("Last name")

        email = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
        email.send_keys("email@com.by")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Element text is wrong")
        browser.quit()


if __name__ == "__main__":
    unittest.main()

