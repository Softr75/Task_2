import requests
import allure
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from utils.helpers import generate_user_data

@allure.feature("Получение заказов")
class TestGetOrders:
    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_orders_authorized(self, user_methods, order_methods):
        payload = generate_user_data()
        create_response = user_methods.create_user(payload)
        token = create_response.json()["accessToken"]

        response = order_methods.get_orders(token)

        assert response.status_code == 200 and response.json()["success"] is True

        user_methods.delete_user(token)

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_orders_unauthorized(self, order_methods):
        response = order_methods.get_orders(token=None)
        print(response.json())
        assert response.status_code == 200 and response.json()["success"] is True
