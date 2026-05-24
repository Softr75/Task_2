import requests
import allure
from utils.data import BASE_URL, ORDER_URL, GET_ORDERS

class OrderMethods:
    def __init__(self):
        self.url = f"{BASE_URL}"
        self.headers = {"Content-Type": "application/json"}

    @allure.step("Создаем заказ")
    def create_order(self, payload, token=None):
        headers = self.headers.copy()

        if token:
            headers["Authorization"] = token

        return requests.post(f"{self.url}{ORDER_URL}", json=payload, headers=headers)

    @allure.step("Получаем заказы")
    def get_orders(self, token):
        headers = self.headers.copy()

        if token:
            headers["Authorization"] = token

        return requests.get(f"{self.url}{GET_ORDERS}", headers=headers)