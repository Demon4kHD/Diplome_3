from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HeaderObjectData:
    '''     URLs    '''
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CONSTRUCTOR_URL = BASE_URL
    ORDERS_LIST_URL = BASE_URL + '/feed'
    PERSONAL_ACCOUNT_URL = BASE_URL + '/login'
    PERSONAL_AUTHORIZE_USER_ACCOUNT_URL = BASE_URL + '/account/profile'
    '''     Locators    '''
    HEADER_OBJECT_CONSTRUCTOR = (By.XPATH, '//*[text()="Конструктор"]')
    HEADER_OBJECT_ORDERS_LIST = (By.XPATH, "//*[text()='Лента Заказов']")
    HEADER_OBJECT_LOGO = (By.XPATH, "//div[contains(@class,'logo')]")
    HEADER_OBJECT_PERSONAL_ACCOUNT = (By.XPATH, '//*[text()="Личный Кабинет"]')
    HEADER_OBJECT_WAIT_CONSTRUCTOR_ELEMENT = (By.XPATH, '//h1[text()="Соберите бургер"]')
    HEADER_OBJECT_WAIT_ORDERS_LIST_ELEMENT = (By.XPATH, '//h1[text()="Лента заказов"]')
    HEADER_OBJECT_WAIT_PERSONAL_ACCOUNT_ELEMENT = (By.XPATH, './/h2[text()="Вход"]')
    HEADER_OBJECT_WAIT_AUTHORIZE_USER_PERSONAL_ACCOUNT_ELEMENT = (By.XPATH, '')


class HeaderObject:
    timeout = 10

    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        self.driver.get(url)

    def get_page_url(self):
        return self.driver.current_url

    def get_user_cookie(self):
        self.driver.get_cookie()

    def add_data_into_data_field(self, elements_locator, data):
        WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            EC.visibility_of_element_located(elements_locator)).send_keys(data)

    def finder_same_element(self, elements_locator):
        return WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            EC.visibility_of_element_located(elements_locator))

    def click_some_element(self, elements_locator):
        self.finder_same_element(elements_locator).click()

    def assert_url(self, elements_locator, expected_url):
        WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            EC.visibility_of_element_located(elements_locator))
        current_url = self.get_page_url()
        assert current_url == expected_url

    def click_constructor_element(self):
        self.click_some_element(HeaderObjectData.HEADER_OBJECT_CONSTRUCTOR)

    def click_oder_list_element(self):
        self.click_some_element(HeaderObjectData.HEADER_OBJECT_ORDERS_LIST)

    def click_personal_account_element(self):
        self.click_some_element(HeaderObjectData.HEADER_OBJECT_PERSONAL_ACCOUNT)
