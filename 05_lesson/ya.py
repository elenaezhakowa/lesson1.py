from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
# driver.find_element(By.CLASS_NAME, "tomatoes")
driver.maximize_window()
# зайти на сайт лабиринт
driver.get("https://www.labirint.ru/")



search_locator='#search-field'
search_imput = driver.find_element(By.CSS_SELECTOR,search_locator)
search_imput.send_keys("Python")

sleep(10)
