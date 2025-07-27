# shop_methods_test.py
import pytest
from selenium import webdriver
from pages.PageObject import PageObject


@pytest.fixture(scope="module")
def firefox_driver():
    """Фикстура для инициализации Firefox драйвера"""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_checkout_process(firefox_driver):
    """
    Авторизация, покупка товаров и проверка итоговой стоимости
    """
    page = PageObject(firefox_driver)

    # Переходим на главную страницу
    page.go_home()

    # Авторизуемся стандартным пользователем
    page.login('standard_user', 'secret_sauce')

    # Ждем загрузки списка товаров
    page.wait_until_products_loaded()

    # Добавляем товары в корзину
    products = {
        'Sauce Labs Backpack': 'add-to-cart-sauce-labs-backpack',
        'Sauce Labs Bolt T-Shirt': 'add-to-cart-sauce-labs-bolt-t-shirt',
        'Sauce Labs Onesie': 'add-to-cart-sauce-labs-onesie'
    }
    page.add_items_to_cart(products)

    # Переходим в корзину
    page.go_to_cart()

    # Начинаем оформление заказа
    page.start_checkout()

    # Заполняем данные покупателя
    page.fill_billing_details('John', 'Doe', '12345')

    # Проверяем итоговую сумму ( $58.29)
    page.check_total_amount('$58.29')

    # Завершаем покупку
    page.complete_order()
