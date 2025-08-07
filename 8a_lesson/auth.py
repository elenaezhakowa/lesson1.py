# import os
# import requests
# import json
# from login_pass import YOUGILE_LOGIN
# from login_pass import YOUGILE_PASSWORD
# from login_pass import YOUGILE_COMPANY_ID


# def get_auth_token():  # Получаем токен авторизации на API Yougile.
#     #  Использует данные из переменных окружения.
#     login = os.getenv("YOUGILE_LOGIN")
#     password = os.getenv("YOUGILE_PASSWORD")


# company_id = os.getenv("YOUGILE_COMPANY_ID")

# auth_data = {
#     "login": YOUGILE_LOGIN,
#     "password": YOUGILE_PASSWORD,
#     "companyId": YOUGILE_COMPANY_ID
# }

# headers = {"Content-Type": "application/json"}

# try:
#     response = requests.post(
#         "https://ru.yougile.com/api-v2/auth/keys",
#         data=json.dumps(auth_data),
#         headers=headers
#     )

#     if response.status_code == 200:
#         return response.json()["key"]
#     else:
#         raise ValueError(response.text)
# except Exception as e:
#     print(f"Ошибка авторизации: {e}")
#     return None
