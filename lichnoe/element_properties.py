from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))
driver.get(" https://ya.ru ")

txt = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").text
print(txt)

tag = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").tag_name
print(tag)


id = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").id
print(id)


href = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']"
                           ).get_attribute("href")
print(href)

# найди мне элемент курса валют и верни значение css_property("font-family")
ff = driver.fInd_element(By.CSS_SELECTOR, "a[title='USD MOEX']"
                         ).value_of_css_property("font-family")
print(ff)

color = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']"
                            ).value_of_css_property("color")
print(color)

sleep(10)
driver. quit()
