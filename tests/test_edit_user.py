import requests
import allure
from methods.user_methods import UserMethods
from utils.helpers import generate_user_data

@allure.feature("Изменение данных пользователя")
class TestEditUser:
    @allure.title("Изменение данных авторизованного пользователя")
    def test_update_user_authorized(self):
        user_methods = UserMethods()
        payload = generate_user_data()
        user_methods.create_user(payload)

        login = user_methods.login_user(
            {"email": payload["email"],
            "password": payload["password"]}
                                        )
        
        token = login.json()["accessToken"]

        update_payload = {
            "name": "newName"
                        }
        response = user_methods.update_user(update_payload, token)

        assert response.status_code == 200 and response.json()["user"]["name"] == "newName"

    @allure.title("Изменение данных неыавторизованного пользователя")
    def test_update_user_unauthorized(self):
        user_methods = UserMethods()

        update_payload = {
            "name": "newName"
                        }
        response = user_methods.update_user(update_payload, None)

        assert response.status_code == 401 and response.json()["message"] == "You should be authorised"