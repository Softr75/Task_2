import allure
from utils.data import INVALID_PAYLOAD, INVALID_LOGIN_MESSAGE

@allure.feature("Логин пользователя")
class TestLoginUser:
    @allure.title("Успешный вход в аккаунт")
    def test_login_user_success(self, user_methods, created_user):
        login_payload = {
            "email": created_user["payload"]["email"],
            "password": created_user["payload"]["password"]
                        }

        response = user_methods.login_user(login_payload)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Вход в аккаунт с некорректными данными")
    def test_login_user_invalid_credentials(self, user_methods):
        response = user_methods.login_user(INVALID_PAYLOAD)

        assert response.status_code == 401 and response.json()["message"] == INVALID_LOGIN_MESSAGE