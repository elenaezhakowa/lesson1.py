# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject:
    def __init__(self, driver):
        self.driver = driver

    def open_calc(self):
        """Открывает страницу калькулятора."""
        self.driver.get(
            'https://bonigarcia.dev/'
            'selenium-webdriver-java/slow-calculator.html')

    def set_delay(self, seconds):
        """Устанавливает задержку в секундах."""
        delay_input = self.driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_buttons(self, *buttons):
        """Кликнуть указанные кнопки калькулятора."""
        for button_text in buttons:
            xpath_selector = f'//span[contains(text(), "{button_text}")]'
            button = self.driver.find_element(By.XPATH, xpath_selector)
            button.click()

    def wait_for_screen_text(self, text, timeout=50):
        """Ждать появления текста на экране калькулятора."""
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '.screen'), text))

    def get_screen_text(self):
        """Получить текст экрана калькулятора."""
        screen = self.driver.find_element(By.CSS_SELECTOR, '.screen')
        return screen.text.strip()
