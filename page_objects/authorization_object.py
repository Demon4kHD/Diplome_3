from objects_data import AuthorizationObjectData as AOD
from page_objects.header_object import HeaderObject as HO


class AuthorizationObject(HO):
    def go_to_authorization_page(self):
        self.go_to_site(AOD.AUTHORIZATION_URL)

    def input_mail_in_field_on_authorization_page(self, email):
        self.add_data_into_data_field(AOD.AUTHORIZATION_PAGE_EMAIL_INPUT, email)

    def input_password_in_field_on_authorization_page(self, password):
        self.add_data_into_data_field(AOD.AUTHORIZATION_PAGE_PASSWORD_INPUT, password)

    def push_on_authorization_button(self):
        self.click_some_element(AOD.AUTHORIZATION_PAGE_SUCCESS_BUTTON)

    def assert_authorization_done(self):
        self.assert_url(AOD.HEADER_OBJECT_WAIT_CONSTRUCTOR_ELEMENT, AOD.BASE_URL + '/')

    def authorization_user(self, current_data, authorization_without_go_to = True):
        if authorization_without_go_to:
            self.go_to_authorization_page()
        self.input_mail_in_field_on_authorization_page(current_data['email'])
        self.input_password_in_field_on_authorization_page(current_data['password'])
        self.push_on_authorization_button()
        self.assert_authorization_done()

    def click_recovery_password_link(self):
        self.click_some_element(AOD.AUTHORIZATION_PAGE_RECOVERY_PASSWORD_LINK)
