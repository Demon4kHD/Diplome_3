import time

from selenium.webdriver.support.wait import WebDriverWait

from objects_data import CreateOrderData as DATA
from page_objects.personal_account_object import PersonalAccountObject as PAGE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class CreateOrderObject(PAGE):
    def assert_goes_to_constructor_page(self):
        self.assert_url(DATA.HEADER_OBJECT_WAIT_CONSTRUCTOR_ELEMENT, DATA.CONSTRUCTOR_URL)

    def assert_goes_to_orders_list_page(self):
        self.assert_url(DATA.HEADER_OBJECT_WAIT_ORDERS_LIST_ELEMENT, DATA.ORDERS_LIST_URL)

    def click_to_ingredient(self, element_selector):
        self.click_some_element(element_selector)

    def click_exit_button_in_dynamic_window(self):
        self.click_some_element(DATA.DYNAMIC_EXIT_BUTTON)

    def assert_dynamic_window(self):
        assert self.get_text_some_element(DATA.DYNAMIC_CALORIES_PRODUCT_COMPOSITION_TEXT) == (
            DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[0])
        assert self.get_text_some_element(DATA.DYNAMIC_PROTEIN_PRODUCT_COMPOSITION_TEXT) == (
            DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[1])
        assert self.get_text_some_element(DATA.DYNAMIC_FAT_PRODUCT_COMPOSITION_TEXT) == (
            DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[2])
        assert self.get_text_some_element(DATA.DYNAMIC_CARBOHYDRATES_PRODUCT_COMPOSITION_TEXT) == (
            DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[3])

    def finder_invisibility_element_of_dynamic_window(self, element):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element(element))

    def assert_close_dynamic_window(self):
        self.finder_same_element(DATA.CHAPTER_INGREDIENTS_MAIN)
        assert self.finder_invisibility_element_of_dynamic_window(DATA.DYNAMIC_WAIT_ELEMENT) != None

    def dragging_ingredient(self, first_element_locator, second_element_locator):
        draggable_ingredient = self.finder_same_element(first_element_locator)
        location_for_drop = self.finder_same_element(second_element_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable_ingredient, location_for_drop).perform()

    def get_count_of_current_ingredient(self):
        return self.get_text_some_element(DATA.test3_bun)

    def assert_count_of_bun(self):
        assert self.get_count_of_current_ingredient() == "2"

    def click_accept_order(self):
        self.click_some_element(DATA.BASKET_ACCEPT_BUTTON)

    def get_order_number(self):
        while self.order_number == '9999':
            self.order_number = self.get_text_some_element(DATA.ACCEPT_ORDER_NUMBER)
        return self.order_number
    """Не смог найти селектор, к которому привязаться, чтобы получить номер заказа не 9999, 
    поэтому решил циклично проверять, что номер заказа не 9999"""

    def create_burger(self):
        self.dragging_ingredient(DATA.INGREDIENT_BUN, DATA.BURGER_BASKET)
        self.dragging_ingredient(DATA.INGREDIENT_MAIN, DATA.BURGER_BASKET)
        self.dragging_ingredient(DATA.INGREDIENT_SAUSE, DATA.BURGER_BASKET)
        self.click_accept_order()
        self.get_order_number()

    def assert_burger_is_created(self):
        assert self.order_number != '9999'
