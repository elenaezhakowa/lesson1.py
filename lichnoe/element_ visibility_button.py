from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))
# зайди на страницу
driver.get(" http://uitestingplayground.com/visibility ")
# посмотри виден ли элемент transparen
is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton"
                                   ).is_displayed()
print(is_displayed)
#  нажать кнопку hide
driver.find_element(By.CSS_SELECTOR, "#hideButton").click()
sleep(2)
# посмотри виден ли элемент transparen
is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton"
                                   ).is_displayed()
print(is_displayed)
sleep(2)
