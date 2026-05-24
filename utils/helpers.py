import uuid

def generate_user_data():
    return {
        "email" : f"{uuid.uuid4()}@yandex.ru",
        "password": "password149",
        "name": "siftr"
            }