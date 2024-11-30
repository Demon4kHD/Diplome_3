import allure

from objects_data import PasswordRecoveryData as DATA


@allure.feature('Проверки Восстановления пароля')
class TestPasswordRecovery:
    data = '12345'

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_recovery_button(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(DATA.AUTHORIZATION_URL)
        page.click_recovery_password_link()
        page.assert_url(DATA.FORGOT_PASSWORD_PAGE_WAIT_ELEMENT, DATA.FORGOT_PASSWORD_URL)

    @allure.title('Ввод почты и клик по кнопке «Восстановить»,')
    def test_inputted_email_and_click_recovery_button(self, is_create_user):
        page, user = is_create_user
        page.go_to_site(DATA.AUTHORIZATION_URL)
        page.click_recovery_password_link()
        inputted_data = user.dict_for_authorization['email']
        page.add_email_into_email_field(inputted_data)
        page.click_recover_button()
        page.assert_url(DATA.RESET_PASSWORD_PAGE_WAIT_ELEMENT, DATA.RESET_PASSWORD_URL)

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_inputted_password_field_active_when_click_eyes_element(self, is_for_reset_password):
        page, user = is_for_reset_password
        page.add_password_into_password_field("password")
        page.add_key_from_message_into_input_field(self.data)
        page.open_input_password_in_field()
        page.assert_inputted_data("password")
