from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.password_recovery_object import PasswordRecoveryData as PRD
from page_objects.password_recovery_object import PasswordRecoveryObject as PRO
from selenium.webdriver.support import expected_conditions as EC


class PersonalAccountData(PRD):
    """Orders history"""
    ORDERS_HISTORY_URL = PRD.BASE_URL + "/account/order-history"
    ORDERS_HISTORY_ACTIVE_LINK = (By.XPATH, '//a[contains(@class,"Account_link_active")]')
    ORDERS_HISTORY_BUTTON = PRD.PERSONAL_HISTORY_ORDERS_LINK_ELEMENT
    ORDERS_HISTORY_BUTTON_TEXT = "История заказов"


class PersonalAccountObject(PRO):
    def click_orders_history(self):
        self.click_some_element(PersonalAccountData.ORDERS_HISTORY_BUTTON)

    def click_exit_button_from_personal_account(self):
        self.click_some_element(PRD.PERSONAL_EXIT_BUTTON)

    def assert_exit_from_personal_account(self):
        self.assert_url(PRD.AUTHORIZATION_PAGE_RECOVERY_PASSWORD_LINK, PRD.AUTHORIZATION_URL)

    def assert_active_element_is_orders_history(self):
        current_text = self.finder_same_element(PersonalAccountData.ORDERS_HISTORY_ACTIVE_LINK).text
        assert current_text == PersonalAccountData.ORDERS_HISTORY_BUTTON_TEXT

    def assert_transition_to_personal_account(self):
        self.assert_url(PRD.HEADER_OBJECT_WAIT_AUTHORIZE_USER_PERSONAL_ACCOUNT_ELEMENT,
                        PRD.PERSONAL_AUTHORIZE_USER_ACCOUNT_URL)