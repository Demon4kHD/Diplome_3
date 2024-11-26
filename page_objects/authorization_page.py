import allure

from objects_data import AuthorizationObjectData as DATA
from page_objects.base_page import BasePage as PageObject


class AuthorizationPage(PageObject):
    @allure.step('Переход на страницу авторизации')
    def go_to_authorization_page(self):
        self.go_to_site(DATA.AUTHORIZATION_URL)

    @allure.step('Ввод почты на странице авторизации')
    def input_mail_in_field_on_authorization_page(self, email):
        self.add_data_into_data_field(DATA.AUTHORIZATION_PAGE_EMAIL_INPUT, email)

    @allure.step('ввод пароля на странице авторизации')
    def input_password_in_field_on_authorization_page(self, password):
        self.add_data_into_data_field(DATA.AUTHORIZATION_PAGE_PASSWORD_INPUT, password)

    @allure.step('Клик по кнопке авторизации')
    def push_on_authorization_button(self):
        self.click_some_element(DATA.AUTHORIZATION_PAGE_SUCCESS_BUTTON)

    @allure.step('Авторизация пройдена?')
    def assert_authorization_done(self):
        self.assert_url(DATA.HEADER_OBJECT_WAIT_CONSTRUCTOR_ELEMENT, DATA.BASE_URL + '/')

    @allure.step('Авторизация пользователя')
    def authorization_user(self, current_data, authorization_without_go_to = True):
        if authorization_without_go_to:
            self.go_to_authorization_page()
        self.input_mail_in_field_on_authorization_page(current_data['email'])
        self.input_password_in_field_on_authorization_page(current_data['password'])
        self.push_on_authorization_button()
        self.assert_authorization_done()

    @allure.step('ажатие на кнопку востановления пароля')
    def click_recovery_password_link(self):
        self.click_some_element(DATA.AUTHORIZATION_PAGE_RECOVERY_PASSWORD_LINK)
