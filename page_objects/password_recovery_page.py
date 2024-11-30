import allure

from objects_data import PasswordRecoveryData as DATA
from page_objects.authorization_page import AuthorizationPage as PageObject


class PasswordRecoveryPage(PageObject):
    @allure.step('Ввод почты в поле ввода')
    def add_email_into_email_field(self, data):
        self.add_data_into_data_field(DATA.FORGOT_PASSWORD_PAGE_EMAIL_INPUT, data)

    @allure.step('Клик на кнопку восстановления пароля')
    def click_recover_button(self):
        self.click_some_element(DATA.FORGOT_PASSWORD_PAGE_RECOVER_BUTTON)

    @allure.step('Добавление пароля в поле ввода')
    def add_password_into_password_field(self, data):
        self.add_data_into_data_field(DATA.RESET_PASSWORD_PAGE_PASSWORDS_INPUT, data)

    @allure.step('Добавление ключа из сообщения в поле ввода')
    def add_key_from_message_into_input_field(self, data):
        self.add_data_into_data_field(DATA.RESET_PASSWORD_PAGE_KEY_FROM_MESSAGE, data)

    @allure.step('Показ введенного пароля')
    def open_input_password_in_field(self):
        self.click_some_element(DATA.RESET_PASSWORD_PAGE_EYES_ELEMENT)

    @allure.step('Проверка введенных данных')
    def assert_inputted_data(self, data):
        current_data = self.finder_same_element(DATA.RESET_PASSWORD_PAGE_ACTIVE_FIELD).get_attribute('value')
        assert current_data == data

