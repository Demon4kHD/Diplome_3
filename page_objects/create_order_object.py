from selenium.webdriver.support.wait import WebDriverWait

from objects_data import CreateOrderData as DATA
from page_objects.personal_account_object import PersonalAccountObject as PAGE
from selenium.webdriver.support import expected_conditions as EC


class CreateOrderObject(PAGE):
    def assert_goes_to_constructor_page(self):
        self.assert_url(DATA.HEADER_OBJECT_WAIT_CONSTRUCTOR_ELEMENT, DATA.CONSTRUCTOR_URL)

    def assert_goes_to_orders_list_page(self):
        self.assert_url(DATA.HEADER_OBJECT_WAIT_ORDERS_LIST_ELEMENT, DATA.ORDERS_LIST_URL)

    def click_to_ingredient(self, element_selector):
        self.click_some_element(element_selector)

    def click_exit_button_in_dynamic_window(self):
        self.click_some_element(DATA.DYNAMIC_EXIT_BUTTON)

    def get_text_from_ingredients_product_composition(self, element_selector):
        return self.finder_same_element(element_selector).get_attribute("textContent")

    def assert_dynamic_window(self):
        assert self.get_text_from_ingredients_product_composition(
            DATA.DYNAMIC_CALORIES_PRODUCT_COMPOSITION_TEXT) == DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[0]
        assert self.get_text_from_ingredients_product_composition(
            DATA.DYNAMIC_PROTEIN_PRODUCT_COMPOSITION_TEXT) == DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[1]
        assert self.get_text_from_ingredients_product_composition(
            DATA.DYNAMIC_FAT_PRODUCT_COMPOSITION_TEXT) == DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[2]
        assert self.get_text_from_ingredients_product_composition(
        DATA.DYNAMIC_CARBOHYDRATES_PRODUCT_COMPOSITION_TEXT) == DATA.DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA[3]

    def finder_invisibility_element_of_dynamic_window(self):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element(DATA.DYNAMIC_WAIT_ELEMENT))

    def assert_close_dynamic_window(self):
        self.finder_same_element(DATA.CHAPTER_INGREDIENTS_MAIN)
        assert self.finder_invisibility_element_of_dynamic_window() != None
