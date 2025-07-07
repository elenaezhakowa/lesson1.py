from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Инициализация сервиса для автоматического скачивания ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# Запуск браузера Google Chrome
driver = webdriver.Chrome(service=service)

# Максимальное расширение окна браузера
driver.maximize_window()

# Переход на целевую страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Нахождение кнопки по классу btn-primary (это синий цвет кнопки)
button = driver.find_element(By.CLASS_NAME, "btn-primary")

# Клик по кнопке
button.click()

# Закрытие браузера после успешного выполнения операции
driver.quit()
