import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from page_objects.personal_account_object import PersonalAccountObject as PAO
from page_objects.personal_account_object import PersonalAccountData as PAD
from api_endpoints.api_endpoints import CreateAndDeleteUserEndpoints as API



@pytest.fixture(params=["firexox"])
# @pytest.fixture(params=['chrome', "firefox"])
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
        # options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        print(f'Sistem hasn`t "{browser_name}", test run with Chrome driver!!!')

    page = PAO(driver)

    yield page
    driver.quit()

@pytest.fixture
def is_create_user(start_driver_and_create_page):
    page = start_driver_and_create_page
    api_user = API()
    api_user.create_user_from_api()

    yield page, api_user
    api_user.delete_user()

@pytest.fixture
def is_for_reset_password(is_create_user):
    page, api_user = is_create_user
    page.go_to_site(PAD.AUTHORIZATION_URL)
    page.click_recovery_password_link()
    inputted_data = api_user.dict_for_authorization['email']
    page.add_email_into_email_field(inputted_data)
    page.click_recover_button()
    return page, api_user

@pytest.fixture
def is_authorize_user(is_create_user):
    page, api_user = is_create_user
    page.authorization_user(api_user.dict_for_authorization)

    return page, api_user
