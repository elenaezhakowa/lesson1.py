# import pytest
# from auth import get_auth_token

# # Будем получать токен один раз на весь набор тестов
# @pytest.fixture(scope="session")
# def token():
#     """Фикстура для получения токена авторизации."""
#     token = get_auth_token()
#     if not token:
#         pytest.fail("Не удалось получить токен авторизации.")
#     return token
