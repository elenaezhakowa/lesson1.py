import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = Options()
driver = webdriver.Edge(options=edge_options)


@pytest.fixture(scope="module")
def browser():
    """Фикстура инициализации веб-драйвера."""
    driver = webdriver.Edge(options=edge_options)
    yield driver
    driver.quit()


def test_fill_and_submit_form(browser):
    # Определение тестового заполнения и отправки формы (браузер)
    """Автотест заполнения и отправки формы."""
    # Переход на целевую страницу
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Поиск полей ввода и заполнение их значениями
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

    for field_id, value in fields_data.items():
        # Для id поля, значения в элементах данных полей()
        input_field = browser.find_element(By.ID, field_id)
        # Поле ввода = элемент поиска в браузере(по.ID, поля ID)
        input_field.clear()  # Очищаем поле на всякий случай
        input_field.send_keys(value)  # Поле ввода ключей отправки(значение)

    # Отправка формы нажатием кнопки Submit
    submit_button = browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ожидание появления классов ошибок/сукцессов
    wait = WebDriverWait(browser, 10)

    # Проверка наличия класса error у поля ZIP code
    zip_code_field = wait.until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="zip-code"]'))
    )
    assert "error" in zip_code_field.get_attribute(
        "class"), "ZIP-код не подсвечен красным!"

    # Проверка успешного заполнения остальных полей
    successful_fields = []
    for field_id in fields_data.keys():
        if field_id != "zip-code":
            field = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f'''//input[@id="{field_id}" and contains(
                     @class, "success")]'''))
            )
            successful_fields.append(field)

    for field in successful_fields:
        assert "success" in field.get_attribute(
            "class"), f"Поле '{field.get_attribute(
                'id')}' не подсвечено зеленым!"
