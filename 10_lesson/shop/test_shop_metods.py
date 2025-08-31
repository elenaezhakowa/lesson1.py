# shop_methods_test.py
import pytest
from selenium import webdriver
from PageObject import PageObject
import allure  # Подключение библиотеки Allure


@allure.epic("Магазин — автоматизированное тестирование оформления заказов")
@pytest.fixture(scope="module")
@allure.title("Инициализация Firefox драйвера")  # Название фикстуры
@allure.link(name="Ссылка", url="https://my.sky.pro/student-c"
                                "abinet/stream-lesson/145745/homework-"
                                "requirements")
def firefox_driver():
    """Фикстура для инициализации Firefox драйвера"""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.feature("Процесс оформления заказа")  # Общая характеристика фичи
@allure.story("Автоматизированная покупка товара")  # История внутри фичи
@allure.description("""
Тест проверки полного цикла покупок:
1. Авторизация
2. Выбор товаров
3. Оформление заказа
""")  # Детальное описание цели теста
def test_checkout_process(firefox_driver):
    """
    Авторизация, покупка товаров и проверка итоговой стоимости
    """
    page = PageObject(firefox_driver)

    with allure.step("Переход на главную страницу"):  # Начало первого шага
        page.go_home()
# Следующий шаг
    with allure.step("Авторизуемся стандартным пользователем"):
        page.login('standard_user', 'secret_sauce')

    with allure.step("Ждем загрузки списка товаров"):  # Очередной шаг
        page.wait_until_products_loaded()

    with allure.step("Добавляем товары в корзину"):  # Ещё один шаг
        products = {
            'Sauce Labs Backpack': 'add-to-cart-sauce-labs-backpack',
            'Sauce Labs Bolt T-Shirt': 'add-to-cart-sauce-labs-bolt-t-shirt',
            'Sauce Labs Onesie': 'add-to-cart-sauce-labs-onesie'
        }
        page.add_items_to_cart(products)

    with allure.step("Переходим в корзину"):  # Новый шаг
        page.go_to_cart()

    with allure.step("Начинаем оформление заказа"):  # Следующий шаг
        page.start_checkout()

    with allure.step("Заполняем данные покупателя"):  # Еще один шаг
        page.fill_billing_details('John', 'Doe', '12345')
# Последний важный шаг
    with allure.step("Проверяем итоговую сумму ($58.29)"):
        page.check_total_amount('$58.29')

    with allure.step("Завершаем покупку"):  # Окончательное завершение
        page.complete_order()
