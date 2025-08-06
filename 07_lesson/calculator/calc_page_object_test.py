import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Фикстура для запуска и остановки драйвера
@pytest.fixture(scope="module")
def chrome_driver():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


# Тестовая функция
def test_calculator_with_delay(chrome_driver):
    # Открываем страницу калькулятора
    chrome_driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    # Настраиваем задержку
    delay_input = chrome_driver.find_element(By.ID, 'delay')
    delay_input.clear()
    delay_input.send_keys('45')

    # Кликаем кнопки
    buttons_to_click = ['7', '+', '8', '=']
    for button_text in buttons_to_click:
        xpath_selector = f'//span[contains(text(), "{button_text}")]'
        button = chrome_driver.find_element(By.XPATH, xpath_selector)
        button.click()

    # Ждем появления результата
    WebDriverWait(chrome_driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), "15"))

    # Проверяем результат
    result_text = chrome_driver.find_element(By.CSS_SELECTOR, '.screen').text
    assert "15" in result_text
    f"Ожидался результат 15, получено: {result_text}"
