import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Импортируем нужный модуль

# Фикстура для открытия браузера


@pytest.fixture(scope="module")
def browser():
    edge_options = Options()
    driver = webdriver.Edge(options=edge_options)
    yield driver
    driver.quit()


def test_fill_and_submit_form(browser):
    # Переходим на целевую страницу
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    browser.implicitly_wait(4)

    # Данные для заполнения форм
    fields_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone-number": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # Заполняем форму
    for field_id, value in fields_data.items():
        input_field = browser.find_element(By.ID, field_id)
        input_field.clear()
        input_field.send_keys(value)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждем появление классов ошибок/сукцессов
    wait = WebDriverWait(browser, 10)

    # Проверяем наличие класса error у поля ZIP code
    zip_code_field = wait.until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="zip-code"]'))
    )
    assert "error" in zip_code_field.get_attribute(
        "class"), "ZIP-код не подсвечен красным!"

    # Проверяем успешность заполнения остальных полей
    successful_fields = []
    for field_id in fields_data.keys():
        if field_id != "zip-code":
            field = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     f'''//input[@id="{field_id}" and contains(@class,
                     "success")
                     ]''')
                )
            )
            successful_fields.append(field)

    for field in successful_fields:
        assert "success" in field.get_attribute(
            "class"), f"""Поле '{field.get_attribute('id')}'
        не подсвечено зеленым!"""


# Обработка таймаута при поиске элемента
wait = WebDriverWait(browser, 10)  # Используем браузер из фикстуры
try:
    first_name_element = wait.until(
        EC.presence_of_element_located((By.ID, 'first-name')))
except TimeoutException:
    print("Элемент не найден!")

# Запуск тестов: pytest --verbose
