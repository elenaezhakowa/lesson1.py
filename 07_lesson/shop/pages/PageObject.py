# page_object.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject:
    def __init__(self, driver):
        self.driver = driver

    def go_home(self):
        """Переходим на домашнюю страницу"""
        self.driver.get('https://www.saucedemo.com/')

    def login(self, username, password):
        """Авторизуемся на сайте"""
        username_field = self.driver.find_element(By.ID, 'user-name')
        password_field = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.ID, 'login-button')

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def wait_until_products_loaded(self):
        """Ждем, пока продукты появятся на странице"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item')))

    def add_items_to_cart(self, items):
        """Добавляем указанные товары в корзину"""
        for item_id in items.values():
            add_cart_button = self.driver.find_element(By.ID, item_id)
            add_cart_button.click()

    def go_to_cart(self):
        """Переходим в корзину"""
        cart_icon = self.driver.find_element(
            By.CLASS_NAME, 'shopping_cart_link')
        cart_icon.click()

    def start_checkout(self):
        """Начинаем оформление заказа"""
        checkout_button = self.driver.find_element(By.ID, 'checkout')
        checkout_button.click()

    def fill_billing_details(self, first_name, last_name, zip_code):
        """Заполняем форму доставки"""
        first_name_field = self.driver.find_element(By.ID, 'first-name')
        last_name_field = self.driver.find_element(By.ID, 'last-name')
        postal_code_field = self.driver.find_element(By.ID, 'postal-code')
        continue_button = self.driver.find_element(By.ID, 'continue')

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        postal_code_field.send_keys(zip_code)
        continue_button.click()

    def check_total_amount(self, expected_total):
        """Проверяем итоговую сумму заказа"""
        total_amount_element = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label')
        total_amount = total_amount_element.text.split(':')[1].strip()
        assert total_amount == expected_total, f"""Итоговая сумма должна быть
        {expected_total}, но была '{total_amount}'"""

    def complete_order(self):
        """Завершаем покупку"""
        finish_button = self.driver.find_element(By.ID, 'finish')
        finish_button.click()
