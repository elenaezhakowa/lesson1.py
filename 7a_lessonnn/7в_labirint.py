from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def test_cart_counter():
    # Добавил переменную searchTerm, которую нужно задать перед использованием
    searchTerm = "Python"

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    # Перейти на сайт Лабиринт.ру
    browser.get("https://www.labirint.ru/")
    # Ожидаем загрузки страницы
    browser.implicitly_wait(4)  # Ждем 4 секунды
    browser.maximize_window()   # Максимизируем окно браузера
    browser.add_cookie(cookie)

    # Поиск товара
    input_field = browser.find_element(By.CSS_SELECTOR, "#search-field")
    input_field.send_keys(searchTerm)
    form = browser.find_element(By.CSS_SELECTOR, "#searchform")
    form.submit()

    # # Переход на страницу результатов поиска
    # results_link = browser.find_element(By.CSS_SELECTOR, 'a[title="таблицей"]')
    # results_link.click()

    # # Ожидание появления таблицы товаров
    # WebDriverWait(browser, 9).until(
    #     EC.presence_of_element_located(
    #         (By.CSS_SELECTOR, 'table.products-table'))
    # )

    # Получение кнопок добавления в корзину
    buttons = browser.find_elements(By.CSS_SELECTOR, 'a.buy-link')
    counter = 0

    for button in buttons:
        button.click()
        counter += 1

    print(f'Нажали {counter} раз')

    # Проверка количества товаров в корзине
    browser.get("https://www.labirint.ru/cart/")
    cart_tab = browser.find_element(
        By.CSS_SELECTOR, '[data-event-label="myCart"]')
    total_count_element = cart_tab.find_element(By.TAG_NAME, 'b')
    total_count = total_count_element.text.strip()

    assert counter == int(
        total_count), f"""
        Количество товаров в корзине не совпадает! Должно быть {counter},
        фактически {total_count}"""
