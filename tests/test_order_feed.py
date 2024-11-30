import allure


@allure.feature('Проверки раздел «Лента заказов»')
class TestOrderFeed:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_from_order_feed_page(self, is_authorize_user_created_order):
        page, user = is_authorize_user_created_order
        page.click_order_list_element()
        current_order = page.create_orders_locator()
        page.open_choiced_order_cart(current_order)
        page.assert_dynamic_window_text()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_two_order_has_in_order_feed(self, authorize_user_created_two_orders):
        page, user = authorize_user_created_two_orders
        page.get_number_orders_from_personal_account()
        page.assert_two_order_in_orders_feed()

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_performed_of_time_is_being_increased(self, is_authorize_user_and_receiving_number_of_orders):
        page, user = is_authorize_user_and_receiving_number_of_orders
        page.create_burger()
        page.switch_tab(False)
        current_number = page.get_numbers_order_feed()
        assert int(current_number) == int(page.counter_completed_today) + 1

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_is_being_filled_out_of_the_day_is_being_increased(self,
                                                                       is_authorize_user_and_receiving_number_of_orders):
        page, user = is_authorize_user_and_receiving_number_of_orders
        page.create_burger()
        page.switch_tab(False)
        current_number = page.get_numbers_order_feed(False)
        assert int(current_number) == int(page.counter_is_completed_for_entire_time) + 1

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_number_appears_in_progress_section(self, open_two_tabs_and_create_order):
        page, user = open_two_tabs_and_create_order
        page.create_burger()
        page.switch_tab(False)
        page.assert_order_in_work()
