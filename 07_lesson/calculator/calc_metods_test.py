import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def chrome_driver():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def open_calc(chrome_driver):
    # Открытие страницы калькулятора
    chrome_driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')


def setting_delay(chrome_driver):
    # Установка задержки на 45 секунд
    delay_input = chrome_driver.find_element(By.ID, 'delay')
    delay_input.clear()
    delay_input.send_keys('45')


def buttons_to_click(chrome_driver):
    # Нажатие кнопок 7 + 8 =
    buttons_to_click = ['7', '+', '8', '=']
    for button_text in buttons_to_click:
        xpath_selector = f'//span[contains(text(), "{button_text}")]'
        button = chrome_driver.find_element(By.XPATH, xpath_selector)
        button.click()


def wait_for_text(driver, selector, expected_text, timeout=50):
    # Ждет появление заданного текста в указанном элементе страницы.
    WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, selector), expected_text))


def extract_text_from_element(driver, selector):
    # Извлекает текст из элемента страницы по указанному селектору.
    return driver.find_element(By.CSS_SELECTOR, selector).text


def check_result(expected_value, actual_value):
    assert expected_value in actual_value, f"""
    Ожидалось значение '{expected_value}', фактически найдено:
    '{actual_value}'"""


def test_calculator(chrome_driver):
    open_calc(chrome_driver)
    setting_delay(chrome_driver)
    buttons_to_click(chrome_driver)
    wait_for_text(chrome_driver, '.screen', '15')
    result_text = extract_text_from_element(chrome_driver, '.screen')
    check_result('15', result_text)
