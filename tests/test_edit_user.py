import allure
from utils.data import UPDATE_PAYLOAD, NO_AUTH_MESSAGE

@allure.feature("Изменение данных пользователя")
class TestEditUser:
    @allure.title("Изменение данных авторизованного пользователя")
    def test_update_user_authorized(self, user_methods, created_user):        
        response = user_methods.update_user(UPDATE_PAYLOAD, created_user["token"])

        assert response.status_code == 200 and response.json()["user"]["name"] == UPDATE_PAYLOAD["name"]

    @allure.title("Изменение данных неавторизованного пользователя")
    def test_update_user_unauthorized(self, user_methods):
        response = user_methods.update_user(UPDATE_PAYLOAD, None)

        assert response.status_code == 401 and response.json()["message"] == NO_AUTH_MESSAGE