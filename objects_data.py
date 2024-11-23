from selenium.webdriver.common.by import By


class HeaderObjectData:

    """     URLs    """
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CONSTRUCTOR_URL = BASE_URL + '/'
    ORDERS_LIST_URL = BASE_URL + '/feed'
    AUTHORIZATION_URL = BASE_URL + '/login'
    PERSONAL_AUTHORIZE_USER_ACCOUNT_URL = BASE_URL + '/account/profile'

    '''     Locators    '''
    HEADER_OBJECT_CONSTRUCTOR = (By.XPATH, '//*[text()="Конструктор"]')
    HEADER_OBJECT_ORDERS_LIST = (By.XPATH, "//*[text()='Лента Заказов']")
    HEADER_OBJECT_LOGO = (By.XPATH, "//div[contains(@class,'logo')]")
    HEADER_OBJECT_PERSONAL_ACCOUNT = (By.XPATH, '//*[text()="Личный Кабинет"]')
    HEADER_OBJECT_WAIT_CONSTRUCTOR_ELEMENT = (By.XPATH, '//h1[text()="Соберите бургер"]')
    HEADER_OBJECT_WAIT_ORDERS_LIST_ELEMENT = (By.XPATH, '//h1[text()="Лента заказов"]')
    HEADER_OBJECT_WAIT_PERSONAL_ACCOUNT_ELEMENT = (By.XPATH, './/h2[text()="Вход"]')
    HEADER_OBJECT_WAIT_AUTHORIZE_USER_PERSONAL_ACCOUNT_ELEMENT = (By.XPATH, '//*[text()="Профиль"]')


class AuthorizationObjectData(HeaderObjectData):

    """Without authorization user"""
    AUTHORIZATION_PAGE_EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    AUTHORIZATION_PAGE_PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    AUTHORIZATION_PAGE_SUCCESS_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    AUTHORIZATION_PAGE_REGISTRATION_LINK = (By.XPATH, '//a[@href="/register"]')
    AUTHORIZATION_PAGE_RECOVERY_PASSWORD_LINK = (By.XPATH, '//a[@href="/forgot-password"]')

    """With authorization user"""
    PERSONAL_ACCOUNT_WITH_AUTHORIZATION_URL = HeaderObjectData.BASE_URL + "/account/profile"
    PERSONAL_PROFILE_LINK_ELEMENT = (By.XPATH, '//a[text()="Профиль"]')
    PERSONAL_HISTORY_ORDERS_LINK_ELEMENT = (By.XPATH, '//a[text()="История заказов"]')
    PERSONAL_EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    PERSONAL_CANSEL_BUTTON = (By.XPATH, '//button[text()="Отмена"]')

    """Forgot passwort page"""
    FORGOT_PASSWORD_WAIT_ELEMENT = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    FORGOT_PASSWORD_URL = HeaderObjectData.BASE_URL + '/forgot-password'


class PasswordRecoveryData(AuthorizationObjectData):

    """     Password recovery page  """
    FORGOT_PASSWORD_PAGE_WAIT_ELEMENT = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    FORGOT_PASSWORD_PAGE_EMAIL_INPUT = (By.XPATH, '//input')
    FORGOT_PASSWORD_PAGE_RECOVER_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')

    """     Password reset page  """
    RESET_PASSWORD_URL = AuthorizationObjectData.BASE_URL + '/reset-password'
    RESET_PASSWORD_PAGE_WAIT_ELEMENT = (By.XPATH, '//button[text()="Сохранить"]')
    RESET_PASSWORD_PAGE_PASSWORDS_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    RESET_PASSWORD_PAGE_EYES_ELEMENT = (By.XPATH, '//div[contains(@class,"input__icon")]')
    RESET_PASSWORD_PAGE_KEY_FROM_MESSAGE = (By.XPATH,
                                            '//label[text()="Введите код из письма"]/following-sibling::input')
    RESET_PASSWORD_PAGE_SAFE_BUTTON = RESET_PASSWORD_PAGE_WAIT_ELEMENT
    RESET_PASSWORD_PAGE_LOGIN_LINK = (By.XPATH, '//a[@href="/login"]')
    RESET_PASSWORD_PAGE_INPUTTED_DATA = (By.XPATH, '//input[@name="Введите новый пароль"]')
    RESET_PASSWORD_PAGE_ACTIVE_FIELD = (By.XPATH,
                                   '//div[contains(@class,"input_status_active")]//input')


class PersonalAccountData(PasswordRecoveryData):

    """Orders history"""
    ORDERS_HISTORY_URL = PasswordRecoveryData.BASE_URL + "/account/order-history"
    ORDERS_HISTORY_ACTIVE_LINK = (By.XPATH, '//a[contains(@class,"Account_link_active")]')
    ORDERS_HISTORY_BUTTON = PasswordRecoveryData.PERSONAL_HISTORY_ORDERS_LINK_ELEMENT
    ORDERS_HISTORY_BUTTON_TEXT = "История заказов"
    ORDERS_HISTORY_NUMBER_ORDER = (By.XPATH, '//p[@class="text text_type_digits-default"]')

class CreateOrderData(PersonalAccountData):

    """Ingredients"""
    CHAPTER_INGREDIENTS_MAIN = (By.XPATH, '//span[text()="Начинки"]')
    INGREDIENT_BUN = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    """Пытался найти каунтер через соседей, но хоть элементы и на одном уровне - элемент не находится.
    Пример:
    test1_bun = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]/following-sibling::div')
    test2_bun = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]/following-sibling::div//p')
    Пришлось делать через индекс элемента в доме"""
    test3_bun = (By.XPATH, '//div[contains(@class,"counter_default")][1]//p[contains(@class,"counter_counter")]')
    INGREDIENT_SAUSE = (By.XPATH, '//p[text()="Соус Spicy-X"]')
    INGREDIENT_MAIN = (By.XPATH, '//p[text()="Мясо бессмертных моллюсков Protostomia"]')

    """Dynamic window about ingredient"""
    DYNAMIC_WAIT_ELEMENT = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    DYNAMIC_EXIT_BUTTON = (By.XPATH,
                           '//section[contains(@class,"Modal_modal_opened")]//button[@type="button"]')
    DYNAMIC_CALORIES_PRODUCT_COMPOSITION_TEXT = (By.XPATH,
                                                 '//p[text()="Калории,ккал"]/following-sibling::p')
    DYNAMIC_PROTEIN_PRODUCT_COMPOSITION_TEXT = (By.XPATH,
                                                '//p[text()="Белки, г"]/following-sibling::p')
    DYNAMIC_FAT_PRODUCT_COMPOSITION_TEXT = (By.XPATH,
                                            '//p[text()="Жиры, г"]/following-sibling::p')
    DYNAMIC_CARBOHYDRATES_PRODUCT_COMPOSITION_TEXT = (By.XPATH,
                                                      '//p[text()="Углеводы, г"]/following-sibling::p')
    DYNAMIC_BUN_PRODUCT_COMPOSITION_DATA = ['643', '85', '26', '44']

    """BASKET"""
    BURGER_BASKET = (By.XPATH, '//div[@class="constructor-element constructor-element_pos_top"]')
    BASKET_ACCEPT_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    """Dynamic window accept order"""
    ACCEPT_WAIT_ELEMENT = (By.XPATH, '/img[@src="https://code.s3.yandex.net/react/code/bun-01.png"]')
    ACCEPT_ORDER_NUMBER = (By.XPATH, '//h2[contains(@class,"Modal_modal__title_shadow")]')
    ACCEPT_ORDER_EXIT_BUTTON = (By.XPATH, '//button[@type="button"][1]')


class OrdersListData(CreateOrderData):
    pass
