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
    PERSONAL_ACCOUNT_AUTHORIZE_USER_URL = HOD.PERSONAL_AUTHORIZE_USER_ACCOUNT_URL
    PERSONAL_ACCOUNT_WITH_AUTHORIZATION_URL = HOD.BASE_URL + "/account/profile"
    PERSONAL_PROFILE_LINK_ELEMENT = (By.XPATH, '//a[text()="Профиль"]')
    PERSONAL_HISTORY_ORDERS_LINK_ELEMENT = (By.XPATH, '//a[text()="История заказов"]')
    PERSONAL_EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    PERSONAL_CANSEL_BUTTON = (By.XPATH, '//button[text()="Отмена"]')
    """Forgot passwort page"""
    FORGOT_PASSWORD_WAIT_ELEMENT = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    FORGOT_PASSWORD_URL = HOD.BASE_URL + '/forgot-password'

class AuthorizationObject(HO):
    def go_to_authorization_page(self):
        self.go_to_site(AuthorizationObjectData.AUTHORIZATION_URL)

    def input_mail_in_field_on_authorization_page(self, email):
        self.add_data_into_data_field(AuthorizationObjectData.AUTHORIZATION_PAGE_EMAIL_INPUT, email)

    def input_password_in_field_on_authorization_page(self, password):
        self.add_data_into_data_field(AuthorizationObjectData.AUTHORIZATION_PAGE_PASSWORD_INPUT, password)

    def push_on_authorization_button(self):
        self.click_some_element(AuthorizationObjectData.AUTHORIZATION_PAGE_SUCCESS_BUTTON)

    def assert_authorization_done(self):
        self.assert_url(AuthorizationObjectData.HEADER_OBJECT_WAIT_CONSTRUCTOR_ELEMENT,
                        AuthorizationObjectData.BASE_URL + '/')

    def authorization_user(self, current_data, authorization_without_go_to = True):
        if authorization_without_go_to == True:
            self.go_to_authorization_page()
        self.input_mail_in_field_on_authorization_page(current_data['email'])
        self.input_password_in_field_on_authorization_page(current_data['password'])
        self.push_on_authorization_button()
        self.assert_authorization_done()

    def click_recovery_password_link(self):
        self.click_some_element(AuthorizationObjectData.AUTHORIZATION_PAGE_RECOVERY_PASSWORD_LINK)
