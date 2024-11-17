from objects_data import PasswordRecoveryData as PRD
from page_objects.authorization_object import AuthorizationObject as AO


class PasswordRecoveryObject(AO):
    def add_email_into_email_field(self, data):
        self.add_data_into_data_field(PRD.FORGOT_PASSWORD_PAGE_EMAIL_INPUT, data)

    def click_recover_button(self):
        self.click_some_element(PRD.FORGOT_PASSWORD_PAGE_RECOVER_BUTTON)

    def add_password_into_password_field(self, data):
        self.add_data_into_data_field(PRD.RESET_PASSWORD_PAGE_PASSWORDS_INPUT, data)

    def add_key_from_message_into_input_field(self, data):
        self.add_data_into_data_field(PRD.RESET_PASSWORD_PAGE_KEY_FROM_MESSAGE, data)

    def click_safe_button(self):
        self.click_some_element(PRD.RESET_PASSWORD_PAGE_SAFE_BUTTON)

    def click_eyes_element(self):
        self.click_some_element(PRD.RESET_PASSWORD_PAGE_EYES_ELEMENT)

    def open_input_password_in_field(self):
        self.click_some_element(PRD.RESET_PASSWORD_PAGE_EYES_ELEMENT)

    def assert_inputted_data(self, data):
        current_data = self.finder_same_element(PRD.RESET_PASSWORD_PAGE_ACTIVE_FIELD).get_attribute('value')
        assert current_data == data

