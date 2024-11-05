import pytest
import requests

import helper


class CreateAndDeleteUserData:
    REGISTRATION_URL = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    DELETE_URL = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    REGISTRATION_BODY = {"email": str,
                         "password": str,
                         "name": str}
    REGISTRATION_BODY_RESPONSE = {"success": True,
                                  "user": {"email": "",
                                           "name": ""},
                                  "accessToken": "Bearer ...",
                                  "refreshToken": ""}
    REGISTRATION_RESPONSE_STATUS_CODE = 200
    REGISTRATION_BODY_SAME_DATA = {"success": False,
                                   "message": "User already exists"}

    AUTHORIZATION_URL = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    AUTHORIZATION_BODY = {"email": "",
                          "password": ""}
    AUTHORIZATION_BODY_RESPONSE = {"success": True,
                                   "accessToken": "Bearer ...",
                                   "refreshToken": "",
                                   "user": {"email": "",
                                            "name": ""}}
    AUTHORIZATION_RESPONSE_STATUS_CODE = 200



class CreateAndDeleteUserEndpoints:
    token = ''
    dict_for_registration, dict_for_authorization = helper.create_json_for_registration_and_authorization()

    def create_user_from_api(self):
        self.response = requests.post(url=CreateAndDeleteUserData.REGISTRATION_URL,
                                      json=self.dict_for_registration)
        response_json = self.response.json()
        self.token = response_json['accessToken']

    def authorization_user(self):
        self.response = requests.post(url=CreateAndDeleteUserData.AUTHORIZATION_URL,
                                      json=self.dict_for_authorization)
        response_json = self.response.json()
        self.token = response_json['accessToken']

        return self.token

    def delete_user(self):
        self.response = requests.delete(url=CreateAndDeleteUserData.DELETE_URL,
                                        headers={"authorization": f'{self.token}'})
        assert self.response.status_code == 202