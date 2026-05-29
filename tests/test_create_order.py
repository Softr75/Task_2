import allure
from utils.data import (ORDER_PAYLOAD_1,
                        ORDER_PAYLOAD_2,
                        EMPTY_PAYLOAD,
                        INVALID_ORDER_PAYLOAD,
                        ORDER_WITHOUT_INGREDIENT_MESSAGE,
                        INVALID_INGREDIENTS_MESSAGE)

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_authorized(self, created_user, order_methods):
        response = order_methods.create_order(ORDER_PAYLOAD_1, created_user["token"])

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создание заказа неавторизованным пользователем")
    def test_create_order_unauthorized(self, order_methods):
        response = order_methods.create_order(ORDER_PAYLOAD_2, token=None)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, order_methods):
        response = order_methods.create_order(EMPTY_PAYLOAD, token=None)

        assert response.status_code == 400 and response.json()["message"] == ORDER_WITHOUT_INGREDIENT_MESSAGE

    @allure.title("Создание заказа с некорректными ингредиентами")
    def test_create_order_with_invalid_ingredients(self, order_methods):
        response = order_methods.create_order(INVALID_ORDER_PAYLOAD, token=None)

        assert response.status_code == 400 and response.json()["message"] == INVALID_INGREDIENTS_MESSAGE