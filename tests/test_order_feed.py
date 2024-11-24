from page_objects.order_feed_object import OrderFeedObject as PageObject
from objects_data import OrderFeedData as DATA


class TestOrderFeed:
    def test_click_order_from_order_feed_page(self, is_authorize_user_created_order):
        page, user = is_authorize_user_created_order
        page.click_order_list_element()
        current_order = page.create_orders_locator()
        page.open_choiced_order_cart(current_order)
        page.assert_dynamic_window_text()

    def test_four_order_has_in_order_feed(self, authorize_user_created_two_orders):
        page, user = authorize_user_created_two_orders
        page.get_number_orders_from_personal_account()
        page.assert_two_order_in_orders_feed()

    def test_test(self, is_authorize_user_and_receiving_number_of_orders):
        page, user = is_authorize_user_and_receiving_number_of_orders
        page.create_burger()
        page.switch_tab(False)
        current_number = page.get_numbers_order_feed()
        assert int(current_number) == int(page.counter_completed_today) + 1
