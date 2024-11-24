from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from objects_data import HeaderObjectData as HOD


class HeaderObject:
    timeout = 10
    order_number = '9999'
    original_window = None
    new_widow = None

    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        self.driver.get(url)

    def get_page_url(self):
        return self.driver.current_url

    def add_data_into_data_field(self, elements_locator, data):
        WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            EC.visibility_of_element_located(elements_locator)).send_keys(data)

    def finder_same_element(self, elements_locator):
        current_element = WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            EC.visibility_of_element_located(elements_locator))
        return current_element

    def click_some_element(self, elements_locator):
        self.finder_same_element(elements_locator).click()

    def get_text_some_element(self, elements_locator):
        element = self.finder_same_element(elements_locator)
        return element.text

    def assert_url(self, elements_locator, expected_url):
        self.finder_same_element(elements_locator)
        assert self.get_page_url() == expected_url

    def click_constructor_element(self):
        self.click_some_element(HOD.HEADER_OBJECT_CONSTRUCTOR)

    def click_order_list_element(self):
        self.click_some_element(HOD.HEADER_OBJECT_ORDERS_LIST)

    def click_personal_account_element(self):
        self.click_some_element(HOD.HEADER_OBJECT_PERSONAL_ACCOUNT)

    def refresh_page(self):
        self.driver.refresh()

    def open_new_tab(self):
        self.original_window = self.driver.current_window_handle
        self.driver.switch_to.new_window('tab')
        self.new_window = self.driver.current_window_handle

    def switch_tab(self, original = True):
        if original == True:
            self.driver.switch_to.window(self.original_window)
        else:
            self.driver.switch_to.window(self.new_window)
