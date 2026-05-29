import allure
from utils.helpers import generate_user_data
from utils.data import EXISTING_USER_MESSAGE, MISSING_FIELDS_MESSAGE

@allure.feature("Создание пользователя")
class TestCreateUser:
    @allure.title("Успешное создание пользователя")
    def test_create_user_success(self, user_methods):
        payload = generate_user_data()
        response = user_methods.create_user(payload)

        assert response.status_code == 200 and response.json()["success"] is True

        token = response.json()["accessToken"]
        user_methods.delete_user(token)

    @allure.title("Создание существующего пользователя")
    def test_create_existing_user(self, user_methods):
        payload = generate_user_data()
        response1 = user_methods.create_user(payload)
        response2 = user_methods.create_user(payload)

        assert response2.status_code in [403, 409] and response2.json()["message"] == EXISTING_USER_MESSAGE

        token = response1.json().get("accessToken")
        if token:
            user_methods.delete_user(token)

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_missing_field(self, user_methods):
        payload = generate_user_data()
        payload.pop("email")
        response = user_methods.create_user(payload)

        assert response.status_code in [403, 409] and response.json()["message"] == MISSING_FIELDS_MESSAGE