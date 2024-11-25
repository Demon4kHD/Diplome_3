import allure

from objects_data import OrderFeedData as DATA
from page_objects.create_order_object import CreateOrderObject as PageObject
from helper import Helper

class OrderFeedObject(PageObject, Helper):
    list_orders = []
    counter_is_completed_for_entire_time = ''
    counter_completed_today = ''

    @allure.step('Открытие выбранной карточки')
    def open_choiced_order_cart(self, cart_locator):
        self.click_some_element(cart_locator)

    @allure.step('Проверка теста динамического окна')
    def assert_dynamic_window_text(self):
        current_text = self.get_text_some_element(DATA.ORDERS_FEED_ASSERT_ELEMENT)
        assert current_text == DATA.ORDERS_FEED_STRUCTURE_ELEMENT

    @allure.step('Создание двух заказов')
    def create_two_orders(self):
        for _ in range(2):
            self.order_number = '9999'
            self.create_burger()
            self.click_some_element(DATA.ACCEPT_ORDER_EXIT_BUTTON)
            self.refresh_page()

    @allure.step('Получить номер заказа из персонального аккаунта')
    def get_number_orders_from_personal_account(self):
        self.click_personal_account_element()
        self.click_orders_history()

        for i in range(1, 3):
            locator = ('xpath', f'//li[{i}]{DATA.ORDERS_HISTORY_NUMBER_ORDER_PATTEN}')
            text = self.get_text_some_element(locator)
            self.list_orders.append(text)
        self.click_order_list_element()

    @allure.step('Проверка двух заказов в Ленте заказов')
    def assert_two_order_in_orders_feed(self):
        number_of_current_orders = 0
        for index in range(2):
            locator = DATA.ORDERS_FEED_TWO_ORDERS_LOCATOR_1 + self.list_orders[index] + DATA.ORDERS_FEED_TWO_ORDERS_LOCATOR_2
            current_element = ('xpath', locator)
            try:
                self.get_text_some_element(current_element)
                number_of_current_orders += 1
            except ValueError:
                print("Заказ отсутствует в ленте заказов")

        assert self.list_orders[0] != self.list_orders[1]
        assert number_of_current_orders == 2

    @allure.step('Получение колличества заказов')
    def get_numbers_order_feed(self, today=True):
        return (self.get_text_some_element(DATA.ORDERS_FEED_TODAY_NUMBERS) if today == True
                else self.get_text_some_element(DATA.ORDERS_FEED_NOT_TODAY_NUMBERS))

    @allure.step("Проверка номера заказа в работе")
    def assert_order_in_work(self):
        locator = ('xpath', f'//li[text()="{self.order_number}"]')
        number_order_in_work = self.get_text_some_element(locator)

        assert number_order_in_work == "0" + self.order_number
