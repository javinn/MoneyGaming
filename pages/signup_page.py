from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class SignUp(Page):

    JOIN_NOW_BUTTON = (By.CSS_SELECTOR, 'a.newUser.green')
    TITLE = (By.ID, 'title')
    TITLES = (By.CSS_SELECTOR, '#title > option')
    FIRST_NAME = (By.ID, 'forename')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="map(lastName)"]')
    REQUIRED_CHECKBOX = (By.CSS_SELECTOR, '#checkbox.required')
    SUBMIT_FORM = (By.ID, 'form')
    DOB_ERROR_MSG = (By.CSS_SELECTOR, 'label[for="dob"]')

    def open_signup(self):
        self.open_url('https://moneygaming.qa.gameaccount.com/sign-up.shtml')

    def select_mr_title(self):
        self.find_element(*self.TITLE).click()
        self.find_elements(*self.TITLES)[1].click()

    def enter_first_name(self):
        self.find_element(*self.FIRST_NAME).send_keys('John')

    def enter_last_name(self):
        self.find_element(*self.LAST_NAME).send_keys('Dough')

    def check_accept_terms(self):
        actions = ActionChains(self.driver)
        checkbox = self.find_element(*self.REQUIRED_CHECKBOX)
        actions.move_to_element(checkbox)
        actions.click()
        actions.perform()

    def submit_form(self):
        self.find_element(*self.SUBMIT_FORM).click()

    def verify_dob_error_msg(self):
        expected_msg_text = 'This field is required'
        self.verify_text(expected_msg_text, *self.DOB_ERROR_MSG)
