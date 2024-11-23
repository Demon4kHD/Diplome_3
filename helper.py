import random

from objects_data import OrderFeedData as DATA


class Helper:
    REGISTRATION_BODY = {"email": str,
                         "password": str,
                         "name": str}
    dict_for_registration = {}
    dict_for_authorization = {}

    def create_random_string(self):
        symbols_for_created_string = 'abcdefghijklmnopqrstuvwxyz0123456789'
        random_string = ''
        for _ in range(9):
            random_string += random.choice(symbols_for_created_string)

        return random_string


    def create_json_for_registration_and_authorization(self):
        for key in self.REGISTRATION_BODY:
            if key == 'email':
                value = self.create_random_string()
                value += '@google.ru'
                self.dict_for_registration[key] = value
                self.dict_for_authorization[key] = value
            else:
                value = self.create_random_string()
                self.dict_for_registration[key] = value
                if key != 'name':
                    self.dict_for_authorization[key] = value

        return self.dict_for_registration, self.dict_for_authorization

    def create_orders_locator(self, index=None):
        if index == None:
            index = random.randint(1,20)
        orders_locator = ('xpath', DATA.ORDERS_LIST_ORDER_CART + f'[{index}]')

        return orders_locator
