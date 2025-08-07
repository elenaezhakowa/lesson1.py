# Импорт библиотек и необходимые модули
from time import sleep
from selenium import webdriver

#  строки подключают драйвер Chrome и менеджер драйверов
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Создается экземпляр веб-драйвера Chrome, который управляет браузером
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))

# Открывается страница Яндекса (https://ya.ru) в браузере.
driver.get(" https://ya.ru ")
# Ищется элемент ввода текста по CSS селектору #text. принимает на вход 2 вещи:
#  тип по которому ищем -локатор и элемент
element = driver.find_element(By.CSS_SELECTOR, "#text")
# очищается его значение
element.clear()
# и вводится строка "test skypro".
element.send_keys("test skypro")
# Нажимается кнопка отправки формы, соответствующая кнопке поиска
driver.find_element(By.CsS_SELECTOR, "button[type=submit]").click()
# Программа ждет 10 секунд, позволяя увидеть результаты поиска
sleep(10)

driver.quit()

# driver. find_elements()
# Метод find_elements() в библиотеке Selenium предназначен для нахождения всех
# элементов на веб-странице, соответствующих заданному критерию поиска. В
# отличие от метода find_element(), который находит лишь первый найденный
# элемент, метод find_elements() возвращает список всех элементов,
# удовлетворяющих указанному условию.

# ▌ Параметры метода:

# find_elements(by, value) принимает два аргумента:

# - by: способ выбора элемента (например, ID, класс, тег, CSS-селектор).
# - value: конкретное значение для поиска (например, название класса,
# id-элемента или текст CSS-селектора).

# Пример использования:

# elements = driver.find_elements(By.CLASS_NAME, 'my-class')
# for element in elements:
#     print(element.text)

# В данном примере мы находим все элементы с классом 'my-class' и выводим их
# текстовые значения.

# ▌ Примеры значений параметра

# Selenium поддерживает различные способы выбора элементов:

# - By.ID: выбор по уникальному идентификатору элемента.
# - By.NAME: выбор по имени атрибута элемента.
# - By.XPATH: выбор по XPath выражению.
# - By.TAG_NAME: выбор по названию HTML-тега.
# - By.CLASS_NAME: выбор по классу элемента.
# - By.CSS_SELECTOR: выбор по CSS-селектору.
# - By.LINK_TEXT: выбор по полному тексту гиперссылки.
# - By.PARTIAL_LINK_TEXT: выбор по частичному совпадению текста гиперссылки.

# Например:

# elements = driver.find_elements(By.XPATH, "//a[@href='example.com']")
# - Найти все ссылки с href="example.com"

# ▌ Зачем нужен?

# Использование find_elements() полезно в случаях, когда нужно обработать
# сразу несколько элементов одной категории, например:

# - Проверить наличие нескольких ссылок с определенным текстом.
# - Собрать коллекцию однотипных элементов (карточки товаров, кнопки навигации
# и т.п.).
# - Получить данные из таблицы, состоящей из множества строк и столбцов.
