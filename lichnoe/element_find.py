# from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))
# зайди на сайт
driver.get(" https://the-internet.herokuapp.com/checkboxes ")
# найди определенный элемент div
div = driver.find_element(By.CSS_SELECTOR, "#page-footer")
# внутри этого divа ищи то, что нам нужно
a = div.find_element(By.CSS_SELECTOR, "a")
print(a.get_attribute("href"))

# найди мне все divы на странице, т.е. это будет список
divs = driver.find_elements(By.CSS_SELECTOR, 'div')
#  сосчитай их
len = len(divs)
print(len)

div = divs(6)                           # найти 6й  div
css_class = div.get_attribute("class")  # и выведи его класс
print(css_class)
