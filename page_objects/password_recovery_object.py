from page_objects.authorization_object import AuthorizationObjectData as AOD
from page_objects.authorization_object import AuthorizationObject as AO
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PasswordRecoveryData(AOD):
    """     Password recovery page  """
    FORGOT_PASSWORD_URL = AOD.BASE_URL + '/forgot-password'
    FORGOT_PASSWORD_PAGE_WAIT_ELEMENT = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    FORGOT_PASSWORD_PAGE_EMAIL_INPUT = (By.XPATH, '//input')
    FORGOT_PASSWORD_PAGE_RECOVER_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    """     Password reset page  """
    RESET_PASSWORD_URL = AOD.BASE_URL + '/reset-password'
    RESET_PASSWORD_PAGE_WAIT_ELEMENT = (By.XPATH, '//button[text()="Сохранить"]')
    RESET_PASSWORD_PAGE_PASSWORDS_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    RESET_PASSWORD_PAGE_EYES_ELEMENT = (By.XPATH, '//div[contains(@class,"input__icon")]')
    RESET_PASSWORD_PAGE_KEY_FROM_MESSAGE = (By.XPATH,
                                            '//label[text()="Введите код из письма"]/following-sibling::input')
    RESET_PASSWORD_PAGE_SAFE_BUTTON = RESET_PASSWORD_PAGE_WAIT_ELEMENT
    RESET_PASSWORD_PAGE_LOGIN_LINK = (By.XPATH, '//a[@href="/login"]')
    RESET_PASSWORD_PAGE_INPUTTED_DATA = (By.XPATH, '//input[@name="Введите новый пароль"]')
    RESET_PASSWORD_PAGE_ACTIVE_FIELD = (By.XPATH,
                                   '//div[contains(@class,"input_status_active")]//input')


class PasswordRecoveryObject(AO):
    def add_email_into_email_field(self, data):
        self.add_data_into_data_field(PasswordRecoveryData.FORGOT_PASSWORD_PAGE_EMAIL_INPUT, data)

    def click_recover_button(self):
        self.click_some_element(PasswordRecoveryData.FORGOT_PASSWORD_PAGE_RECOVER_BUTTON)

    def add_password_into_password_field(self, data):
        self.add_data_into_data_field(PasswordRecoveryData.RESET_PASSWORD_PAGE_PASSWORDS_INPUT, data)

    def add_key_from_message_into_input_field(self, data):
        self.add_data_into_data_field(PasswordRecoveryData.RESET_PASSWORD_PAGE_KEY_FROM_MESSAGE, data)

    def click_safe_button(self):
        self.click_some_element(PasswordRecoveryData.RESET_PASSWORD_PAGE_SAFE_BUTTON)

    def click_eyes_element(self):
        self.click_some_element(PasswordRecoveryData.RESET_PASSWORD_PAGE_EYES_ELEMENT)

    def open_input_password_in_field(self):
        self.click_some_element(PasswordRecoveryData.RESET_PASSWORD_PAGE_EYES_ELEMENT)

    def assert_inputted_data(self, data):
        current_data = WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            EC.visibility_of_element_located(PasswordRecoveryData.RESET_PASSWORD_PAGE_ACTIVE_FIELD)).get_attribute(
            'value')
        assert current_data == data

