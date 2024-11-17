from page_objects.password_recovery_object import PasswordRecoveryData as PRD
from page_objects.password_recovery_object import PasswordRecoveryObject as PRO


class TestPasswordRecovery:
    data = '12345'
    def test_click_recovery_button(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(PRD.PERSONAL_ACCOUNT_URL )
        page.click_recovery_password_link()
        page.assert_url(PRD.FORGOT_PASSWORD_PAGE_WAIT_ELEMENT, PRD.FORGOT_PASSWORD_URL)

    def test_inputted_email_and_click_recovery_button(self, is_create_user):
        page, user = is_create_user
        page.go_to_site(PRD.PERSONAL_ACCOUNT_URL)
        page.click_recovery_password_link()
        inputted_data = user.dict_for_authorization['email']
        page.add_email_into_email_field(inputted_data)
        page.click_recover_button()
        page.assert_url(PRD.RESET_PASSWORD_PAGE_WAIT_ELEMENT, PRD.RESET_PASSWORD_URL)

    def test_inputted_password_field_active_when_click_eyes_element(self, is_for_reset_password):
        page, user = is_for_reset_password
        page.add_password_into_password_field("password")
        page.add_key_from_message_into_input_field(self.data)
        page.open_input_password_in_field()
        page.assert_inputted_data("password")
