from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager. chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))
driver.implicitly_wait(18)                                   # повиси 18 секунд
driver.get(" http://uitestingplayground.com/ajax ")         # зайди на страницу
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()  
#                                              найди эту кнопку и кликни на нее
content = driver.find_element(By.CSS_SELECTOR, "#content")
#                                                           найди этот элемент
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
#                                                          возьми у него текст
print(txt)                                                # выведи этот текст
sleep(5)
