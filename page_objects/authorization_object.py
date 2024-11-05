from page_objects.header_object import HeaderObjectData as HOD
from page_objects.header_object import HeaderObject as HO
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthorizationObjectData(HOD):
    """Without authorization user"""
    AUTHORIZATION_URL = HOD.PERSONAL_ACCOUNT_URL
    AUTHORIZATION_PAGE_EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    AUTHORIZATION_PAGE_PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    AUTHORIZATION_PAGE_SUCCESS_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    AUTHORIZATION_PAGE_REGISTRATION_LINK = (By.XPATH, '//a[@href="/register"]')
    AUTHORIZATION_PAGE_RECOVERY_PASSWORD_LINK = (By.XPATH, '//a[@href="/forgot-password"]')
    """With authorization user"""


class AuthorizationObject(HO):
    def go_to_authorization_page(self):
        self.driver.get(AuthorizationObjectData.AUTHORIZATION_URL)

    def input_mail_in_field_on_authorization_page(self, email):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(AuthorizationObjectData.AUTHORIZATION_PAGE_EMAIL_INPUT)).send_keys(email)

    def input_password_in_field_on_authorization_page(self, password):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(AuthorizationObjectData.AUTHORIZATION_PAGE_PASSWORD_INPUT)).send_keys(password)

    def push_on_authorization_button(self):
        self.click_some_element(AuthorizationObjectData.AUTHORIZATION_PAGE_SUCCESS_BUTTON)

    def assert_authorization_done(self):
        self.assert_url(AuthorizationObjectData.HEADER_OBJECT_WAIT_CONSTRUCTOR_ELEMENT,
                        AuthorizationObjectData.BASE_URL)

    def push_on_forgot_password_link(self):
        self.click_some_element(AuthorizationObjectData.AUTHORIZATION_PAGE_RECOVERY_PASSWORD_LINK)

    def assert_forgot_password_to_go(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(AuthorizationObjectData.FORGOT_PASSWORD_PAGE_WAIT_ELEMENT))
        assert self.driver.get_url() == FPD.FORGOT_PASSWORD_URL


    def authorization_user(self, current_data, authorization_without_go_to = True):
        if authorization_without_go_to == True:
            self.go_to_authorization_page()
        self.input_mail_in_field_on_authorization_page(current_data['email'])
        self.input_password_in_field_on_authorization_page(current_data['password'])
        self.push_on_authorization_button()
        self.assert_authorization_done()

    def go_to_forgot_password_page(self):
        self.push_on_forgot_password_link()
        self.assert_forgot_password_to_go()

    def click_recovery_password_link(self):
        self.click_some_element(AuthorizationObjectData.AUTHORIZATION_PAGE_RECOVERY_PASSWORD_LINK)
