import allure

from objects_data import PersonalAccountData as DATA
from page_objects.password_recovery_page import PasswordRecoveryPage as PRO


class AccountPage(PRO):
    @allure.step('Клик на историю заказов')
    def click_orders_history(self):
        self.click_some_element(DATA.ORDERS_HISTORY_BUTTON)

    @allure.step('Клин на кнопку выхода')
    def click_exit_button_from_personal_account(self):
        self.click_some_element(DATA.PERSONAL_EXIT_BUTTON)

    @allure.step('Проверка выхода из персонального аккаунта')
    def assert_exit_from_personal_account(self):
        self.assert_url(DATA.AUTHORIZATION_PAGE_RECOVERY_PASSWORD_LINK, DATA.AUTHORIZATION_URL)

    @allure.step('Проверка активного элемента')
    def assert_active_element_is_orders_history(self):
        current_text = self.finder_same_element(DATA.ORDERS_HISTORY_ACTIVE_LINK).text
        assert current_text == DATA.ORDERS_HISTORY_BUTTON_TEXT

    @allure.step('Проверка перехода в персональный аккаунт')
    def assert_transition_to_personal_account(self):
        self.assert_url(DATA.HEADER_OBJECT_WAIT_AUTHORIZE_USER_PERSONAL_ACCOUNT_ELEMENT,
                        DATA.PERSONAL_AUTHORIZE_USER_ACCOUNT_URL)

    @allure.step('Получение номера заказа и ленты заказов профиля')
    def get_order_number_from_personal_account(self):
        current_number = self.finder_same_element(DATA.ORDERS_HISTORY_NUMBER_ORDER).text
        assert_number = current_number[1:]
        return assert_number

    @allure.step('Проверка номера заказа в персональном аккаунте')
    def assert_order_number_from_personal_account(self):
        checking_number = "0" + self.order_number
        assert self.get_order_number_from_personal_account() == checking_number
