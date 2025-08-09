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

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
# перейти на сайт лабиринта
    browser.get("https://www.labirint.ru/")
    # Ожидаем загрузки страницы
    browser.implicitly_wait(4)  # ждем 4 секунды
    browser.maximize_window()  # делаем максимальный размер окна
    browser.add_cookie(cookie)
    browser.find_element(
        By.CSS_SELECTOR, '#search-field').send_keys(searchTerm)
    browser. find_element(By.CSS_SELECTOR, '#searchform'). submit()
    browser. find_element(By. CSS_SELECTOR,
                          'a[title=таблицей]').click()

    WebDriverWait(browser, 9).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'table.products-table')))
    buttons = browser.find_elements(By.CSS_SELECTOR,'a. buy-link')
counter =0
for i in range(0, len(buttons)):
    buttons [i].click()
counter = counter + 1
print('Нажали' + str(counter) + 'раз')
browser.get('https://www.labirint.ru/'+'cart/')
tab = browser.find_element(
    By.CSS_SELECTOR,'[data-event-label="myCart"]')
num = tab.find_element(By.TAG_NAME, 'b')
total = num.text
assert counter == int(total)
