# После установки вы можете проверить, что Selenium установлен и работает
# корректно, запустив следующий код:

from selenium import webdriver

# Пример для Google Chrome
driver = webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.title)
driver.quit()
