INVALID_PAYLOAD = {
    "email": "invalid@yandex.ru",
    "password": "wrongpassword",
                    }

ORDER_PAYLOAD_1 = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d",
        "61c0c5a71d1f82001bdaaa6e"]
                        }

ORDER_PAYLOAD_2 = {
        "ingredients": ["61c0c5a71d1f82001bdaaa76",
        "61c0c5a71d1f82001bdaaa74"]
                    }

EMPTY_PAYLOAD = {
        "ingredients": []
                    }

INVALID_ORDER_PAYLOAD = {
        "ingredients": ["60d3b41abdacab0026a733c6",
        "000000000000000000000000"]
                            }

UPDATE_PAYLOAD = {"name": "newName"}


ORDER_WITHOUT_INGREDIENT_MESSAGE = "Ingredient ids must be provided"
INVALID_INGREDIENTS_MESSAGE = "One or more ids provided are incorrect"
EXISTING_USER_MESSAGE = "User already exists"
MISSING_FIELDS_MESSAGE = "Email, password and name are required fields"
INVALID_LOGIN_MESSAGE = "email or password are incorrect"
NO_AUTH_MESSAGE = "You should be authorised"