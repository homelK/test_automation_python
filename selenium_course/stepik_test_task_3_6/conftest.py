import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="ru", help="choose a preferable language for a browser"
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("--language")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--lang={browser_language}")
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chrome_options)
    yield browser
    browser.quit()