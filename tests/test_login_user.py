import requests
import allure
from methods.user_methods import UserMethods
from utils.data import INVALID_PAYLOAD
from utils.helpers import generate_user_data

@allure.feature("Логин пользователя")
class TestLoginUser:
    @allure.title("Успешный вход в аккаунт")
    def test_login_user_success(self):
        user_methods = UserMethods()
        payload = generate_user_data()

        create_response = user_methods.create_user(payload)

        login_payload = {
            "email": payload["email"],
            "password": payload["password"]
                        }

        response = user_methods.login_user(login_payload)

        assert response.status_code == 200 and response.json()["success"] is True

        token = create_response.json()["accessToken"]
        user_methods.delete_user(token)

    @allure.title("Вход в аккаунт с некорректными данными")
    def test_login_user_invalid_credentials(self):
        user_methods = UserMethods()
        response = user_methods.login_user(INVALID_PAYLOAD)

        assert response.status_code == 401 and response.json()["message"] == "email or password are incorrect"