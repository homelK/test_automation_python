import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chrome_options)
    yield browser
    browser.quit()
