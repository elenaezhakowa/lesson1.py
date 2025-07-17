from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Автоматически устанавливаем и настраиваем geckodriver для Firefox
service = FirefoxService(executable_path=GeckoDriverManager().install())

# Инициализируем браузер Firefox
driver = webdriver.Firefox(service=service)

try:
    # Открываем страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")

    # Находим поля для ввода логина и пароля
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Вводим данные
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")

    # Находим кнопку Login и нажимаем её
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Получаем текст уведомления (предположительно, оно появится после
    #  успешной авторизации)
    success_message = (
        driver.find_element(By.CLASS_NAME, "flash.success").text.strip())

    # Выводим текст уведомления в консоль
    print(f"Успешное уведомление: {success_message}")
    sleep(10)
finally:
    # Закрываем браузер
    driver.quit()
