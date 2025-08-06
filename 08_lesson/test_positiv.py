import pytest
import json
import requests


# Фикстура для получения токена авторизации на API Yougile
@pytest.fixture(scope="module")
def get_token():
    auth_data = {
        "login": "",
        "password": "",
        "companyId": ""  # ID компании
    }

    headers = {'Content-Type': 'application/json'}  # Заголовки HTTP-запроса

# Отправляем POST-запрос на сервер для получения ключа авторизации
    response = requests.post(
        'https://ru.yougile.com/api-v2/auth/keys',
        data=json.dumps(auth_data),  # Преобразование данных в JSON
        headers=headers              # Передача заголовков
    )
    token = response.json()['key']
    yield token


# Фикстура для получения списка пользователей


@pytest.fixture(scope="module")
def get_user_list(get_token):
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {get_token}'  # Заголовки с токеном
               }                                       # авторизации

# Отправляем GET-запрос для получения списка пользователей
    response = requests.get(
        'https://ru.yougile.com/api-v2/users',
        headers=headers
    )
    print(response.json())  # Печать полученного ответа (для дебага)
    # return response.json()  # Возврат списка пользователей
    get_user_list(
        'wFzmL19-oVF3PbmZkvc24qkcZwJrgIXed1V2zIlZLL84TenO1710En9ZzUD4R0Mf')


# Тест на создание нового проекта
def test_create_project(get_token):
    project_data = {
        "title": "ГосУслуги",  # Название проекта
        "users": {                       # Пользователь и роль
            'ff02d87a-5e23-4082-971d-d1f2ae3edf86': "admin"
        }
    }

# Заголовки с токеном авторизации
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {get_token}'}

# Отправляем POST-запрос для создания проекта
    response = requests.post(
        'https://ru.yougile.com/api-v2/projects',
        data=json.dumps(project_data),  # Данные проекта в виде JSON
        headers=headers                 # Заголовки запроса
    )
    # Печать результата операции (для дебага)
    print(response.json())

    # Утверждение успешного статуса ответа (ожидаем 201 Created)
    assert response.status_code == 201


# Тест на обновление существующего проекта
def test_edit_project(get_token):
    edit_data = {
        "deleted": False,              # Проект не удалён
        "title": "ГосУслуги1",         # Новое название проекта
        "users": {                     # Пользователь и роль
            'ff02d87a-5e23-4082-971d-d1f2ae3edf86': "admin"
        }
    }
    # Заголовки с токеном авторизации
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {get_token}'}

    # Отправляем PUT-запрос для обновления проекта
    response = requests.put(
        'https://ru.yougile.com/api-v2/projects/'
        '003400df-16f3-4452-83f9-f5e03d48f5cd',
        data=json.dumps(edit_data),     # Обновленные данные проекта
        headers=headers                 # Заголовки запроса
    )
    # Печать результата операции (для дебага)
    print(response.json())

    # Утверждение успешного статуса ответа (ожидаем 200 OK)
    assert response.status_code == 200


# Тест на связывание проекта с пользователями
def test_bind_by_id(get_token):
    auth_data = {
        "title": "ГосУслуги1",  # Название проекта
        "users": {              # Пользователь и роль
            'ff02d87a-5e23-4082-971d-d1f2ae3edf86': "admin"
        }
    }
    # Заголовки с токеном авторизации
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {get_token}'}
    # Отправляем POST-запрос для связывания проекта с пользователями
    response = requests.get(
        'https://ru.yougile.com/api-v2/projects/'
        '003400df-16f3-4452-83f9-f5e03d48f5cd',
        data=json.dumps(auth_data),             # Данные проекта
        headers=headers                         # Заголовки запроса

    )
    # Печать результата операции (для дебага)
    print(response.json())

    # Утверждение успешного статуса ответа (ожидаем 201 Created)

    assert response.status_code == 200
