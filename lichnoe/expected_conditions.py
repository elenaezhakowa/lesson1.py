from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
#                         библиотека с ожидаемыми условиями: дождись этого и...
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))
# жди 40 секунд и отправляй запрос каждые 0.1сек
waiter = WebDriverWait(driver, 40, 0.1)
# зайди на сайт
driver.get(" http://uitestingplayground.com/progressbar ")
# найди кнопку старт и нажми  ее
driver.find_element(By.CSS_SELECTOR, "#startButton").click()
# дождись пока progressBar достигнез текста 75%
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#progressBar"
                                               ), "75%"))
# найди кнопку стоп и нажми ее
driver.find_element(By.CSS_SELECTOR, "#stopButton").click()
# выведи результат текстом
print(driver.find_element(By.CSs_SELECTOR, "#result").text)
