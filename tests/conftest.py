import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from page_objects.password_recovery_object import PasswordRecoveryObject as PRO
from page_objects.password_recovery_object import PasswordRecoveryData as PRD
from api_endpoints.api_endpoints import CreateAndDeleteUserEndpoints as API



@pytest.fixture(params=['chrome'])
def start_driver_and_create_page(request):
    browser_name = request.param
    driver = None
    options = Options()
    options.add_argument("--headless")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    else:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    page = PRO(driver)

    yield page

    driver.quit()

@pytest.fixture
def is_authorize_user(start_driver_and_create_page):
    page = start_driver_and_create_page
    api_user = API()
    api_user.create_user_from_api()

    yield page, api_user
    api_user.delete_user()

@pytest.fixture
def is_for_reset_password(is_authorize_user):
    page, api_user = is_authorize_user
    page.go_to_site(PRD.PERSONAL_ACCOUNT_URL)
    page.click_recovery_password_link()
    inputted_data = api_user.dict_for_authorization['email']
    page.add_email_into_email_field(inputted_data)
    page.click_recover_button()
    return page, api_user

