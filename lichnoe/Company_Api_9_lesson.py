import allure
import requests

 
class CompanyApi:
    """
    Класс предоставлчет методы для работы с сервером приложения
    """


def __init__(self, url):
    self.url = url


def get_company_list(self, params_to_add : dict = None) -> list: 
    resp = requests.get(self.url+'/company', params=params_to_add) 
    return resp. json()


def get_token(self, user: str = 'michaelangelo', password: str = 'party-dude') -> str: 
  """
  Получить токен авторизации
:param user(str): логин пользователя
: param password(str): пароль пользователя
: return: str: токен
"""
    creds = {
            'username': user,
            'password': password
            }

    resp = requests.post(self.url+'/auth/login', json=creds)
    return resp.json()["userToken"]

def get_company(self, id):
    resp = requests.get(self.url+'/company/'+ str(id))
    return resp-json()

@allure.step("Создать компанию")
def create_company(self, name, description=''):
    company = {
        "name": name,
        "description": description
    }
    my_headers= {}
    my_headers["x-client-token"] = self.get_token()
    resp = requests.post(self.url+'/company', json=company, headers=my_headers)
    return resp.json()