from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запускаем браузер Chrome
driver = webdriver.Chrome()

try:
    # Открываем страницу демонстрации
    driver.get("http://uitestingplayground.com/visibility")

    # Найдем кнопку 'Hide'
    hide_button = driver.find_element(By.ID, "hideButton")

    # Кнопка нажимается?
    print(f"Кнопка 'Hide' видима: {hide_button.is_displayed()}")

    # Жмем на кнопку 'Hide', чтобы скрыть другие элементы
    hide_button.click()

    # Подождем немного, пока страница обновится
    time.sleep(1)

    # Проверяем состояние остальных кнопок
    show_button = driver.find_element(By.ID, "showButton")
    print(f"Кнопка 'Show' видима: {show_button.is_displayed()}")

finally:
    # Закроем браузер
    driver.quit()
