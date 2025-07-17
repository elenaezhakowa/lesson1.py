from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка браузера
driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/ajax')

try:
    # Ждем появления кнопки запуска AJAX-запроса
    blue_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, 'ajaxButton')))

    # Кликаем по кнопке
    blue_button.click()

    # Ждем появления текста на зеленой плашке
    green_box = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'bg-success')))

    # Выводим текст из зеленой плашки
    print(green_box.text)

finally:
    # Закрываем браузер
    driver.quit()
