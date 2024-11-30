import requests

from helper import Helper


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



class CreateAndDeleteUserEndpoints(Helper):
    token = ''

    def create_user_from_api(self):
        self.dict_for_registration, self.dict_for_authorization = self.create_json_for_registration_and_authorization()
        response = requests.post(url=CreateAndDeleteUserData.REGISTRATION_URL,
                                      json=self.dict_for_registration)
        response_json = response.json()
        self.token = response_json['accessToken']

    def authorization_user(self):
        response = requests.post(url=CreateAndDeleteUserData.AUTHORIZATION_URL,
                                      json=self.dict_for_authorization)
        response_json = response.json()
        self.token = response_json['accessToken']

        return self.token

    def delete_user(self):
        response = requests.delete(url=CreateAndDeleteUserData.DELETE_URL,
                                        headers={"authorization": f'{self.token}'})
        assert response.status_code == 202