import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import json

@pytest.fixture(scope="session")
def login(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    login_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "ember458")))
    login_btn.click()

    with open("secrets", "r") as credentials:
        content = json.load(credentials)
        login = content["login_stepik"]
        passw = content["password_stepik"]


    input_email = browser.find_element(By.NAME, "login")
    input_email.send_keys(login)

    input_pass = browser.find_element(By.NAME, "password")
    input_pass.send_keys(passw)

    submit_btn = browser.find_element(By.XPATH, '//button[contains(@class, "sign-form__btn")]')
    submit_btn.click()

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(@class, "rubricator-dropdown__toggler")]')))


@pytest.mark.parametrize("lesson", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_answers(login, browser, lesson):

    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)

    textarea = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))

    if textarea.get_attribute("disabled"):
        try_again_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(@class,"again-btn")]')))
        try_again_btn.click()
        textarea = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))

    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))

    submit_answer_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="submit-submission"]')))
    submit_answer_btn.click()

    feedback_text = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//p[@class="smart-hints__hint"]')))
    text = feedback_text.text

    assert text == "Correct!", f"Expected 'Correct' but got '{text}'"



