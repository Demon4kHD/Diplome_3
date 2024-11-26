import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from objects_data import HeaderObjectData as DATA


class HeaderObject:
    timeout = 20
    order_number = '9999'
    original_window = None
    new_widow = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу')
    def go_to_site(self, url):
        self.driver.get(url)

    @allure.step('Получить URL страницы')
    def get_page_url(self):
        return self.driver.current_url

    @allure.step('Получение значения в поле ввода')
    def add_data_into_data_field(self, elements_locator, data):
        WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            EC.visibility_of_element_located(elements_locator)).send_keys(data)

    @allure.step('Поиск элемента')
    def finder_same_element(self, elements_locator):
        current_element = WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            EC.visibility_of_element_located(elements_locator))
        return current_element

    @allure.step('Клик по элементу')
    def click_some_element(self, elements_locator):
        self.finder_same_element(elements_locator).click()

    @allure.step('Получить текст элемента')
    def get_text_some_element(self, elements_locator):
        element = self.finder_same_element(elements_locator)
        return element.text

    @allure.step('Проверка URL')
    def assert_url(self, elements_locator, expected_url):
        self.finder_same_element(elements_locator)
        assert self.get_page_url() == expected_url

    @allure.step('Клик на Конструктор в Хедере')
    def click_constructor_element(self):
        self.click_some_element(DATA.HEADER_OBJECT_CONSTRUCTOR)

    @allure.step('Клик на Ленту заказов в Хедере')
    def click_order_list_element(self):
        self.click_some_element(DATA.HEADER_OBJECT_ORDERS_LIST)

    @allure.step('Клик на Профиль в Хедере')
    def click_personal_account_element(self):
        self.click_some_element(DATA.HEADER_OBJECT_PERSONAL_ACCOUNT)

    @allure.step('Обновление страницы')
    def refresh_page(self):
        self.driver.refresh()

    @allure.step('Открытие новой вкладки')
    def open_new_tab(self):
        self.original_window = self.driver.current_window_handle
        self.driver.switch_to.new_window('tab')
        self.new_window = self.driver.current_window_handle

    @allure.step('Переключение вкладки')
    def switch_tab(self, original = True):
        if original == True:
            self.driver.switch_to.window(self.original_window)
        else:
            self.driver.switch_to.window(self.new_window)
