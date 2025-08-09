import requests

base_url = "https://x-clients-be.onrender.com"

# получить список всех компаний


def test_get_companies():
    resp = requests.get(base_url+"/company")
    body = resp.json()

    assert resp.status_code == 200
    assert len(body) > 0

# получить список активных компаний


def test_get_active_companies():
    resp = requests.get(base_url+"/company")
    full_list = resp.json()

    my_params = {'active': 'true'}
    resp = requests.get(base_url+"/company", params=my_params)
    filtered_list = resp.json()
# проверить что список 1 больше чем спиок 2
    assert len(full_list) > len(filtered_list)


def test_add_new():
    # получить количество компаний
    # создать новую компанию
    # получить количество компаний
    # проверить что компания добавилась
    # проверить название и описание последней компании
    # проверить что ID последней компании равен ответу из шага 2
