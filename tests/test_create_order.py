import requests
import allure
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from utils.helpers import generate_user_data

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_authorized(self, user_methods, order_methods):
        payload = generate_user_data()

        create_response = user_methods.create_user(payload)
        token = create_response.json()["accessToken"]

        order_payload = {
                "ingredients": ["61c0c5a71d1f82001bdaaa6d",
                                "61c0c5a71d1f82001bdaaa6e"]
                        }
        response = order_methods.create_order(order_payload, token)

        assert response.status_code == 200 and response.json()["success"] is True

        user_methods.delete_user(token)

    @allure.title("Создание заказа неавторизованным пользователем")
    def test_create_order_unauthorized(self, order_methods):
        order_payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa76",
                            "61c0c5a71d1f82001bdaaa74"]
                    }

        response = order_methods.create_order(order_payload, token=None)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, order_methods):
        order_payload = {
            "ingredients": []
                        }

        response = order_methods.create_order(order_payload, token=None)

        assert response.status_code == 400 and response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с некорректными ингредиентами")
    def test_create_order_with_invalid_ingredients(self, order_methods):
        order_payload = {
            "ingredients": ["60d3b41abdacab0026a733c6",
                            "000000000000000000000000"]
                            }
        response = order_methods.create_order(order_payload, token=None)

        assert response.status_code == 400 and response.json()["message"] == "One or more ids provided are incorrect"