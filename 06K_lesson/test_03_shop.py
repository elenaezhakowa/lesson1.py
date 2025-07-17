import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def firefox_driver():
    gecko_service = Service('/path/to/geckodriver')
    # замените путь на геко-драйвер Firefox
    driver = webdriver.Firefox(service=gecko_service)
    yield driver
    driver.quit()


def test_checkout_process(firefox_driver):
    """
    Авторизация, покупка товаров и проверка итоговой стоимости
    """
    # Открыть главную страницу
    firefox_driver.get('https://www.saucedemo.com/')

    # Авторизация стандартным пользователем
    username_field = firefox_driver.find_element(By.ID, 'user-name')
    password_field = firefox_driver.find_element(By.ID, 'password')
    login_button = firefox_driver.find_element(By.ID, 'login-button')

    username_field.send_keys('standard_user')
    password_field.send_keys('secret_sauce')
    login_button.click()

    # Подождать загрузки главной страницы продуктов
    WebDriverWait(firefox_driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item'))
    )

    # Добавить три товара в корзину
    products = {
        'Sauce Labs Backpack': 'add-to-cart-sauce-labs-backpack',
        'Sauce Labs Bolt T-Shirt': 'add-to-cart-sauce-labs-bolt-t-shirt',
        'Sauce Labs Onesie': 'add-to-cart-sauce-labs-onesie'
    }

    for item_id in products.values():
        add_cart_button = firefox_driver.find_element(By.ID, item_id)
        add_cart_button.click()

    # Перейти в корзину
    cart_icon = firefox_driver.find_element(
        By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.click()

    # Оформить заказ
    checkout_button = firefox_driver.find_element(By.ID, 'checkout')
    checkout_button.click()

    # Заполнить личные данные
    first_name_field = firefox_driver.find_element(By.ID, 'first-name')
    last_name_field = firefox_driver.find_element(By.ID, 'last-name')
    postal_code_field = firefox_driver.find_element(By.ID, 'postal-code')
    continue_button = firefox_driver.find_element(By.ID, 'continue')

    first_name_field.send_keys('John')
    last_name_field.send_keys('Doe')
    postal_code_field.send_keys('12345')
    continue_button.click()

    # Завершить покупку и проверить сумму
    finish_button = firefox_driver.find_element(By.ID, 'finish')
    finish_button.click()

    total_amount_element = firefox_driver.find_element(
        By.CLASS_NAME, 'summary_total_label')
    total_amount = total_amount_element.text.split(':')[1].strip()

    # Проверить итоговую сумму ($58.29)
    assert total_amount == '$58.29', f"""Итоговая сумма
    должна быть $58.29, но была '{total_amount}'"""
