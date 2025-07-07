from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Автоматическая установка и настройка geckodriver
service = FirefoxService(executable_path=GeckoDriverManager().install())

# Инициализация браузера Firefox
driver = webdriver.Firefox(service=service)

try:
    # Открываем целевую страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим единственное поле ввода на странице
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Вводим текст "Sky"
    input_field.send_keys("Sky")

    # Очищаем поле ввода
    input_field.clear()

    # Вводим новый текст "Pro"
    input_field.send_keys("Pro")

finally:
    # Закрываем браузер
    driver.quit()
