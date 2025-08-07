# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait


# @pytest.fixture(scope="module")
# def driver():
#     # Укажите путь к драйверу вашего браузера
#     if 'Edge' in webdriver.__dict__:
#         browser = webdriver.Edge()  # Используем Microsoft Edge
#     elif 'Safari' in webdriver.__dict__:
#         browser = webdriver.Safari()  # Используем Apple Safari
#     else:
#         raise Exception("Browser not supported.")

#     yield browser
#     browser.quit()


# def test_fill_and_submit_form(driver):
#     """Автотест заполнения формы"""
#     # Открываем веб-страницу
#     driver.get(
#         'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

#     # Заполняем поля формы
#     first_name_field = driver.find_element(By.NAME, 'firstName')
#     last_name_field = driver.find_element(By.NAME, 'lastName')
#     address_field = driver.find_element(By.NAME, 'address')
#     email_field = driver.find_element(By.NAME, 'email')
#     phone_number_field = driver.find_element(By.NAME, 'phoneNumber')
#     zip_code_field = driver.find_element(By.NAME, 'zipCode')
#     city_field = driver.find_element(By.NAME, 'city')
#     country_field = driver.find_element(By.NAME, 'country')
#     job_position_field = driver.find_element(By.NAME, 'jobPosition')
#     company_field = driver.find_element(By.NAME, 'company')

#     submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

#     first_name_field.send_keys('Иван')
#     last_name_field.send_keys('Петров')
#     address_field.send_keys('Ленина, 55-3')
#     email_field.send_keys('test@skypro.com')
#     phone_number_field.send_keys('+7985899998787')
#     zip_code_field.clear()  # Оставляем ZIP-код пустым
#     city_field.send_keys('Москва')
#     country_field.send_keys('Россия')
#     job_position_field.send_keys('QA')
#     company_field.send_keys('SkyPro')

#     # Нажимаем кнопку Submit
#     submit_button.click()

#     # Ожидаем появления результатов проверки полей
#     wait = WebDriverWait(driver, 30)
#     error_class = '.is-invalid'
#     success_class = '.is-valid'

#     # Проверяем, что Zip-code выделен красным цветом (ошибка)
#     assert len(wait.until(
#         lambda d: d.find_elements(By.CSS_SELECTOR, f'{error_class}')
#     )) > 0, "Ошибка не отображается для поля Zip Code."

#     # Проверяем, что остальные поля выделены зелёным цветом (успех)
#     valid_fields = wait.until(
#         lambda d: d.find_elements(By.CSS_SELECTOR, f'{success_class}')
#     )
#     for field in valid_fields:
#         print(f"Поле {field.get_attribute('name')} успешно заполнено.")


import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def firefox_driver():
    gecko_service = Service('/path/to/geckodriver')
    # Замените на ваш путь к geckodriver
    driver = webdriver.Firefox(service=gecko_service)
    yield driver
    driver.quit()


def test_checkout_process(firefox_driver):
    """
    Авторизация, покупка товаров и проверка итоговой стоимости
    """
    try:
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
        assert total_amount == '$58.29', f"""Ожидалась сумма $58.29,
        но указана '{total_amount}'"""

    except Exception as e:
        print(f"Тест завершился неудачей: {e}")
        raise
    # Повторно бросаем исключение вверх, чтобы оно было видно в отчетах Pytest
