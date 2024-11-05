import random


REGISTRATION_BODY = {"email": str,
                     "password": str,
                     "name": str}
dict_for_registration = {}
dict_for_authorization = {}

def create_random_string():
    symbols_for_created_string = 'abcdefghijklmnopqrstuvwxyz0123456789'
    random_string = ''
    for _ in range(9):
        random_string += random.choice(symbols_for_created_string)

    return random_string


def create_json_for_registration_and_authorization():
    for key in REGISTRATION_BODY:
        if key == 'email':
            value = create_random_string()
            value += '@google.ru'
            dict_for_registration[key] = value
            dict_for_authorization[key] = value
        else:
            value = create_random_string()
            dict_for_registration[key] = value
            if key != 'name':
                dict_for_authorization[key] = value

    return dict_for_registration, dict_for_authorization
