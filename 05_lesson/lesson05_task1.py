from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Настройка и запуск браузера Chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Максимизируем окно браузера
driver.maximize_window()

# Переходим на страницу
driver.get("http://uitestingplayground.com/classattr")

# Находим кнопку по CSS-классу и кликаем на нее
button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
button.click()

sleep(10)
driver.quit()
