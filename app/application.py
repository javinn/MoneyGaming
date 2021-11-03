from pages.base_page import Page
from pages.signup_page import SignUp


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(self.driver)
        self.sign_up = SignUp(self.driver)

