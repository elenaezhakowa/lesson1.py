from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome. service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))
# ключ -нейм - куки полиси - валуе 1
my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

driver.get(" https://labirint.ru ")
driver.add_cookie(my_cookie)
# перезапустим страницу
driver. refresh()
# посмотреть все куки
cookies = driver.get_cookies()
print(cookies)
# удаляем куки
driver.delete_cookie
# перезапустить страницу
driver.refresh
# повисит 10 сек
sleep(10)
# закрываем сайт
driver.quit()
