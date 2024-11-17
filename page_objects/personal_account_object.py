from selenium.webdriver.common.by import By

from objects_data import PersonalAccountData as PAD
from page_objects.password_recovery_object import PasswordRecoveryObject as PRO


class PersonalAccountObject(PRO):
    def click_orders_history(self):
        self.click_some_element(PAD.ORDERS_HISTORY_BUTTON)

    def click_exit_button_from_personal_account(self):
        self.click_some_element(PAD.PERSONAL_EXIT_BUTTON)

    def assert_exit_from_personal_account(self):
        self.assert_url(PAD.AUTHORIZATION_PAGE_RECOVERY_PASSWORD_LINK, PAD.AUTHORIZATION_URL)

    def assert_active_element_is_orders_history(self):
        current_text = self.finder_same_element(PAD.ORDERS_HISTORY_ACTIVE_LINK).text
        assert current_text == PAD.ORDERS_HISTORY_BUTTON_TEXT

    def assert_transition_to_personal_account(self):
        self.assert_url(PAD.HEADER_OBJECT_WAIT_AUTHORIZE_USER_PERSONAL_ACCOUNT_ELEMENT,
                        PAD.PERSONAL_AUTHORIZE_USER_ACCOUNT_URL)