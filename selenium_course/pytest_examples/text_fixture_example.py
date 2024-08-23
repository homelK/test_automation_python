from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


# class TestMainPage1:
#
#     @classmethod
#     def setup_class(cls):
#         print("\nIn setup: ", id(cls))
#         print("\nstart browser for test suite..")
#         cls.browser = webdriver.Chrome()
#
#     @classmethod
#     def teardown_class(cls):
#         print("\nIn teardown: ", id(cls))
#         print("\nquit browser for test suite..")
#         cls.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         print("\nFirst test method: ", id(self))
#         self.browser.get(link)
#         self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         print("\nLast test method: ", id(self))
#         self.browser.get(link)
#         self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("\nSetup method: ", id(self))
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("\nTeardown method: ", id(self))
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print("\nFirst test method: ", id(self))
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("\nLast test method: ", id(self))
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")