import allure
import pytest

from objects_data import CreateOrderData as DATA


@allure.feature('Проверка основного функционала')
class TestGeneralFunctions:
    @allure.title('Переход по клику на «Конструктор» с Главной страницы')
    def test_click_constructor_link_from_base_page(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(DATA.BASE_URL)
        page.click_constructor_element()
        page.assert_goes_to_constructor_page()

    @allure.title('Переход по клику на «Конструктор» с других страниц')
    @pytest.mark.parametrize('url', [DATA.AUTHORIZATION_URL,
                                     DATA.RESET_PASSWORD_URL,
                                     DATA.ORDERS_LIST_URL])
    def test_click_constructor_link_from_others_page(self, start_driver_and_create_page, url):
        page = start_driver_and_create_page
        page.go_to_site(url)
        page.click_constructor_element()
        page.assert_goes_to_constructor_page()

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_to_orders_list(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(DATA.BASE_URL)
        page.click_oder_list_element()
        page.assert_goes_to_orders_list_page()

    @allure.title('Клик на ингредиент, появится всплывающее окно с деталями')
    def test_click_to_ingredient(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(DATA.BASE_URL)
        page.click_to_ingredient(DATA.INGREDIENT_BUN)
        page.assert_dynamic_window()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_click_to_exit_button_into_dynamic_window(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(DATA.BASE_URL)
        page.click_to_ingredient(DATA.INGREDIENT_BUN)
        page.click_exit_button_in_dynamic_window()
        page.assert_close_dynamic_window()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_increasing_account_ingredient(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(DATA.BASE_URL)
        page.dragging_ingredient(DATA.INGREDIENT_BUN, DATA.BURGER_BASKET)
        page.assert_count_of_bun()

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorize_user_can_create_order(self, is_authorize_user):
        page, user = is_authorize_user
        page.create_burger()
        page.assert_burger_is_created()
