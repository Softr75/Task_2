import requests
import allure
from utils.config import BASE_URL, REGISTER_URL, LOGIN_URL, USER_URL
from utils.helpers import generate_user_data

class UserMethods:
    def __init__(self):
        self.url = f"{BASE_URL}"
        self.headers = {"Content-Type": "application/json"}

    @allure.step("Создаем пользователя")
    def create_user(self, payload=None):
        if payload is None:
            data = generate_user_data()
            payload = {
                    "email": data["email"],
                    "password": data["password"],
                    "name": data["name"]
                    }
        return requests.post(f"{self.url}{REGISTER_URL}", json=payload, headers=self.headers)

    @allure.step("Логиним пользователя")
    def login_user(self, payload):
        return requests.post(f"{self.url}{LOGIN_URL}", json=payload, headers=self.headers)

    @allure.step("Удаляем пользователя")
    def delete_user(self, token):
        headers = {
            "Authorization": token}
        return requests.delete(f"{self.url}{USER_URL}", headers=headers)
 
    @allure.step("Обновляем пользователя")
    def update_user(self, payload, token):
        headers = {
            "Authorization": token}
        return requests.patch(f"{self.url}{USER_URL}", json=payload, headers=headers)