import allure
from selenium.webdriver.support.wait import WebDriverWait

from objects_data import CreateOrderData as DATA
from page_objects.account_page import AccountPage as PAGE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class ConstructorPage(PAGE):
    @allure.step('Проверка перехода на страницу Конструктор')
    def assert_goes_to_constructor_page(self):
        self.assert_url(DATA.HEADER_OBJECT_WAIT_CONSTRUCTOR_ELEMENT, DATA.CONSTRUCTOR_URL)

    @allure.step('Проверка перехода на страницу Лента заказов')
    def assert_goes_to_orders_list_page(self):
        self.assert_url(DATA.HEADER_OBJECT_WAIT_ORDERS_LIST_ELEMENT, DATA.ORDERS_LIST_URL)

    @allure.step('Клик по ингредиенту')
    def click_to_ingredient(self, element_selector):
        self.click_some_element(element_selector)

    @allure.step('Клик на кнопку закрытия динамического окна')
    def click_exit_button_in_dynamic_window(self):
        self.click_some_element(DATA.DYNAMIC_EXIT_BUTTON)

    @allure.step('Проверка, что динамическое окно открыто')
    def assert_dynamic_window(self):
        assert self.get_text_some_element(DATA.DYNAMIC_CALORIES_PRODUCT_COMPOSITION_TEXT) == (
            DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[0])
        assert self.get_text_some_element(DATA.DYNAMIC_PROTEIN_PRODUCT_COMPOSITION_TEXT) == (
            DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[1])
        assert self.get_text_some_element(DATA.DYNAMIC_FAT_PRODUCT_COMPOSITION_TEXT) == (
            DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[2])
        assert self.get_text_some_element(DATA.DYNAMIC_CARBOHYDRATES_PRODUCT_COMPOSITION_TEXT) == (
            DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[3])

    @allure.step('Элемент закрыт другим элементом')
    def finder_invisibility_element_of_dynamic_window(self, element):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element(element))

    @allure.step('Проверка закрытия динамического окна')
    def assert_close_dynamic_window(self):
        self.finder_same_element(DATA.CHAPTER_INGREDIENTS_MAIN)
        assert self.finder_invisibility_element_of_dynamic_window(DATA.DYNAMIC_WAIT_ELEMENT) != None

    @allure.step('Перетягивание ингредиента')
    def dragging_ingredient(self, first_element_locator, second_element_locator):
        draggable_ingredient = self.finder_same_element(first_element_locator)
        location_for_drop = self.finder_same_element(second_element_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable_ingredient, location_for_drop).perform()

    @allure.step('Получение каунтера ингредиента')
    def get_count_of_current_ingredient(self):
        return self.get_text_some_element(DATA.test3_bun)

    @allure.step('Проверка каунтера булки')
    def assert_count_of_bun(self):
        assert self.get_count_of_current_ingredient() == "2"

    @allure.step('Клик на кнопку подтверждения заказа')
    def click_accept_order(self):
        self.click_some_element(DATA.BASKET_ACCEPT_BUTTON)

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        while self.order_number == '9999':
            self.order_number = self.get_text_some_element(DATA.ACCEPT_ORDER_NUMBER)
        return self.order_number
    """Не смог найти селектор, к которому привязаться, чтобы получить номер заказа не 9999, 
    поэтому решил циклично проверять, что номер заказа не 9999"""

    @allure.step('Создание заказа')
    def create_burger(self):
        self.dragging_ingredient(DATA.INGREDIENT_BUN, DATA.BURGER_BASKET)
        self.dragging_ingredient(DATA.INGREDIENT_MAIN, DATA.BURGER_BASKET)
        self.dragging_ingredient(DATA.INGREDIENT_SAUSE, DATA.BURGER_BASKET)
        self.click_accept_order()
        self.get_order_number()

    @allure.step('Проверка, что бургер создан')
    def assert_burger_is_created(self):
        assert self.order_number != '9999'
