import pytest

from objects_data import CreateOrderData as DATA


class TestGeneralFunctions:
    def test_click_constructor_link_from_base_page(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(DATA.BASE_URL)
        page.click_constructor_element()
        page.assert_goes_to_constructor_page()

    @pytest.mark.parametrize('url', [DATA.AUTHORIZATION_URL,
                                     DATA.RESET_PASSWORD_URL,
                                     DATA.ORDERS_LIST_URL])
    def test_click_constructor_link_from_others_page(self, start_driver_and_create_page, url):
        page = start_driver_and_create_page
        page.go_to_site(url)
        page.click_constructor_element()
        page.assert_goes_to_constructor_page()

    def test_click_to_orders_list(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(DATA.BASE_URL)
        page.click_oder_list_element()
        page.assert_goes_to_orders_list_page()

    def test_click_to_ingredient(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(DATA.BASE_URL)
        page.click_to_ingredient(DATA.INGREDIENT_BUN)
        page.assert_dynamic_window()

    def test_click_to_exit_button_into_dynamic_window(self, start_driver_and_create_page):
        page = start_driver_and_create_page
        page.go_to_site(DATA.BASE_URL)
        page.click_to_ingredient(DATA.INGREDIENT_BUN)
        page.click_exit_button_in_dynamic_window()
        page.assert_close_dynamic_window()
