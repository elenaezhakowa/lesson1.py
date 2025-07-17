from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу тестирования
    driver.get('http://uitestingplayground.com/textinput')

    # Заполняем текстовое поле значением 'SkyPro'
    input_field = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
    input_field.send_keys('SkyPro')

    # Нажимаем синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
    button.click()

    # Получаем обновленный текст кнопки и выводим в консоль
    updated_button_text = button.text
    print(updated_button_text)
    sleep(5)
finally:
    # Закрываем браузер
    driver.quit()
