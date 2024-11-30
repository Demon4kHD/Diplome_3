import allure

from objects_data import OrderFeedData as DATA


@allure.feature('Проверка Личного кабинета')
class TestPersonalAccount:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_click_to_personal_account_link_from_header(self, is_authorize_user):
        page, api_user = is_authorize_user
        page.click_personal_account_element()
        page.assert_transition_to_personal_account()

    @allure.title('Переход в раздел «История заказов»')
    def test_click_orders_history_link(self, is_authorize_user):
        page, api_user = is_authorize_user
        page.click_personal_account_element()
        page.click_orders_history()
        page.assert_active_element_is_orders_history()

    @allure.title('Переход в раздел «История заказов» при наличии у пользователя заказа')
    def test_click_orders_history_link_for_user_with_order(self, is_authorize_user_created_order):
        page, user = is_authorize_user_created_order
        page.go_to_site(DATA.BASE_URL)
        page.click_personal_account_element()
        page.click_orders_history()
        page.assert_order_number_from_personal_account()

    @allure.title('Выход из аккаунта')
    def test_click_exit_button(self, is_authorize_user):
        page, api_user = is_authorize_user
        page.click_personal_account_element()
        page.click_exit_button_from_personal_account()
        page.assert_exit_from_personal_account()
