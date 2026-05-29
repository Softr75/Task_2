import allure

@allure.feature("Получение заказов")
class TestGetOrders:
    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_orders_authorized(self, created_user, order_methods):
        response = order_methods.get_orders(created_user["token"])

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_orders_unauthorized(self, order_methods):
        response = order_methods.get_orders(token=None)

        assert response.status_code == 200 and response.json()["success"] is True