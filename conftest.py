import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from page_objects.order_feed_object import OrderFeedObject as PageObject
from objects_data import OrderFeedData as DATA
from api_endpoints.api_endpoints import CreateAndDeleteUserEndpoints as API


@allure.step('Выбор и запуск выбранного драйвера')
@pytest.fixture(params=['chrome', "firefox"])
def start_driver_and_create_page(request):
    browser_name = request.param
    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        print(f'Sistem hasn`t "{browser_name}", test run with Chrome driver!!!')

    page = PageObject(driver)

    yield page
    driver.quit()

@allure.step('Создание тестового пользователя через АПИ и удаление его после теста')
@pytest.fixture
def is_create_user(start_driver_and_create_page):
    page = start_driver_and_create_page
    api_user = API()
    api_user.create_user_from_api()

    yield page, api_user
    api_user.delete_user()

@allure.step('Авторизация ранее созданного пользователя и ввод электронной почты в пле восстановления пароля')
@pytest.fixture
def is_for_reset_password(is_create_user):
    page, api_user = is_create_user
    page.go_to_site(DATA.AUTHORIZATION_URL)
    page.click_recovery_password_link()
    inputted_data = api_user.dict_for_authorization['email']
    page.add_email_into_email_field(inputted_data)
    page.click_recover_button()
    return page, api_user

@allure.step('Авторизация ранее созданного пользователя')
@pytest.fixture
def is_authorize_user(is_create_user):
    page, api_user = is_create_user
    page.authorization_user(api_user.dict_for_authorization)

    return page, api_user

@allure.step('Авторизация ранее созданного пользователя и создание заказа')
@pytest.fixture
def is_authorize_user_created_order(is_authorize_user):
    page, api_user = is_authorize_user
    page.create_burger()
    page.click_some_element(DATA.ACCEPT_ORDER_EXIT_BUTTON)

    return page, api_user

@allure.step('Авторизация ранее созданного пользователя и создание двух заказом')
@pytest.fixture
def authorize_user_created_two_orders(is_authorize_user):
    page, api_user = is_authorize_user
    page.create_two_orders()

    return page, api_user

@allure.step('Авторизованный пользователь получает номера созданных заказов в личном кабинете')
@pytest.fixture
def is_authorize_user_and_receiving_number_of_orders(is_authorize_user):
    page, api_user = is_authorize_user
    page.open_new_tab()
    page.go_to_site(DATA.BASE_URL)
    page.click_order_list_element()
    page.counter_completed_today = page.get_numbers_order_feed(True)
    page.counter_is_completed_for_entire_time = page.get_numbers_order_feed(False)
    page.switch_tab()

    return page, api_user

@allure.step('Открытие второй вкладки и создание заказа')
@pytest.fixture
def open_two_tabs_and_create_order(is_authorize_user):
    page, api_user = is_authorize_user
    page.open_new_tab()
    page.go_to_site(DATA.BASE_URL)
    page.click_order_list_element()
    page.switch_tab()

    return page, api_user
