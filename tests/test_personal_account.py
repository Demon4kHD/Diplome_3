from objects_data import OrdersListData as DATA


class TestPersonalAccount:

    def test_click_to_personal_account_link_from_header(self, is_authorize_user):
        page, api_user = is_authorize_user
        page.click_personal_account_element()
        page.assert_transition_to_personal_account()

    def test_click_orders_history_link(self, is_authorize_user):
        page, api_user = is_authorize_user
        page.click_personal_account_element()
        page.click_orders_history()
        page.assert_active_element_is_orders_history()

    def test_click_orders_history_link_for_user_with_order(self, is_authorize_user_created_order):
        page, user = is_authorize_user_created_order
        page.go_to_site(DATA.BASE_URL)
        page.click_personal_account_element()
        page.click_orders_history()
        page.assert_order_number_from_personal_account()

    def test_click_exit_button(self, is_authorize_user):
        page, api_user = is_authorize_user
        page.click_personal_account_element()
        page.click_exit_button_from_personal_account()
        page.assert_exit_from_personal_account()
