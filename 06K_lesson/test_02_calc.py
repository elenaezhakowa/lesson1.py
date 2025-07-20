# import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def chrome_driver():
    service = Service(executable_path='/path/to/chromedriver')
    # Путь к вашему chromedriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_calculator_with_delay(chrome_driver):
    """
    Автотест калькулятора с задержкой вычисления
    """
    # Открытие страницы
    chrome_driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    # Установка задержки на 45 секунд
    delay_input = chrome_driver.find_element(By.ID, 'delay')
    delay_input.clear()
    delay_input.send_keys('45')

    # Нажатие кнопок 7 + 8 =
    buttons_to_click = ['7', '+', '8', '=']
    for button_text in buttons_to_click:
        xpath_selector = f'//span[contains(text(), "{button_text}")]'
        button = chrome_driver.find_element(By.XPATH, xpath_selector)
        button.click()

    # Ждем пока результат появится
    result_element = WebDriverWait(chrome_driver, 50).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'screen'))
    )

    # Получение результата и проверка значения
    actual_result = result_element.text.strip()
    assert actual_result == '15', f"""
    Ожидалось число 15, получено {actual_result}"""
