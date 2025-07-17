from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открытие веб-драйвера
driver = webdriver.Chrome()

try:
    # Перейти на указанный сайт
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждем пока загрузится третья картинка
    wait = WebDriverWait(driver, 40)
    third_image = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#award'))
    )

    # Извлекаем значение атрибута src третьей картинки
    third_image_src = third_image.get_attribute("src")

    # Выводим значение в консоль
    print(third_image_src)

finally:
    # Закрываем браузер
    driver.quit()
