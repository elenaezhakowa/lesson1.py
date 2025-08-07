# from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome. service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver. support import expected_conditions as EC

cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def test_cart_counter():

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
# перейти на сайт лабиринта
    browser.get("https://www.labirint.ru/")
    # Ожидаем загрузки страницы
    browser.implicitly_wait(4)  # ждем 4 секунды
    browser.maximize_window()  # делаем максимальный размер окна

    # WebDriverWait(browser, 10).until(EC.presence_of_element_located(
    # (By.TAG_NAME, "body")))
    browser.add_cookie(cookie)

# Поиск книг по слову 'python'
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

# Добавление всех книг с первой страницы в корзину
    # buy_buttons = browser.find_elements(
    #     By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    # for btn in buy_buttons:
    #     btn.click()

# # найти все книги по слову python
#     # найди элемент такой-то и в него введи пайтон
#     browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
#     # найди элемент -кнопка "искать" и нажми(тег button, атрибут type)
#     browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

# переключиться на таблицу: кликни на переключалку таблицы
    # browser.find_element(By.CSS_SELECTOR, 'a[title="таблицей]').click()
    # # дальше в течениe 10сек. жди когда почвится элемент таблица
    # WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    # )
    # sleep(5)  # ждем 5 сек
# добавить все книги в корзину и посчитать, сколько
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, 'a._btn.btn-tocart.buy-link')
    counter = 0
    for btn in buy_buttons:
        btn. click()
        counter += 1

        print(counter)

# перейти в корзину
# поверить счетчик товаров. Должен быть равен числу нажатий
    browser.quit()
