import pytest
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods
from utils.helpers import generate_user_data

@pytest.fixture
def user_methods():
    return UserMethods()

@pytest.fixture
def order_methods():
    return OrderMethods()

@pytest.fixture
def created_user(user_methods):
    payload = generate_user_data()
    create_response = user_methods.create_user(payload)

    token = create_response.json()["accessToken"]

    yield {
        "payload": payload,
        "response": create_response,
        "token": token
            }

    user_methods.delete_user(token)