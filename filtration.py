from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import re
import time
# Параметры фильтрации

days = 20 # Дней с момента последней публикации
acc_subscriptions = 500 # Количество подписок у аккаунта
publications = 10 # Количество публикаций у аккаунта

browser = webdriver.Chrome("E:\Gittext\chromedriver.exe")

# Проверка существования элемента на странице

def xpath_existence (url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence



# Считывание списка аккаунтов
f = open("E:\Gittext\spisok.txt", 'r')
file_list = []
for line in f:
    file_list.append(line)
f.close()

filtered_list = [] # Отфильтрованый список
i = 0 # количество подходячих пользователей
j = 0 # номер вывода в терминале


for person in file_list:
    """Основной цикл для фильтрации по всем параметрам, если аккаунт не подходит под
    заданные параметры - пропускаем его через continue и ищем дальше """
    j += 1
    browser.get(person)
    time.sleep(0.6)

    # Проверка закрытости аккаунта

    element = '//section/main/div/div/article/div/div/h2'
    if xpath_existence(element) == 1:
        try:
            if browser.find_element_by_xpath(element).text == "This Account is Private" or "Это закрытый аккаунт":
                print(j, "Приватный аккаунт")
                continue
        except StaleEleentReferenceException:
            print ("Ошибка, код ошибки - 1")

    # Проверка на количество подписок

    element = "//section/main/div/header/section/ul/li[3]/a/span"
    if xpath_existence(element) == 0:
        print (j, "Код ошибки - 2")
        continue
    status = browser.find_element_by_xpath(element).text
    status = re.sub(r'\s', '', status) # удаление пробелов из числа подписок (в коде xpath)

    if int(status) > acc_subscriptions:
        print (j, "У аккаунта больше ", acc_subscriptions, "подписок")
        continue

    # Проверка ссылки на сайт (коммерческий ли аккаунт)

    element = "//section/main/div/header/section/div[2]/a"
    if xpath_existence(element) == 1:
        print(j, "Есть ссылка на сайт, пропускаем")
        continue

    # Проверка на наличие публикаций в аккаунте

    element = "//section/main/div/header/section/ul/li[1]/a/span"
    if xpath_existence(element) == 0:
        print(j, "Ошибка")
        continue
    status = browser.find_element_by_xpath(element).text #повторение кода!
    status = re.sub(r'\s', '', status) # удаление пробелов из числа подписок (в коде xpath)
    if int(status) < publications:
        print (j, "У аккаунта меньше ", publications, "публикаций")
        continue

    # Добавление пользователя в отфильтрованный файл

    filtered_list.append(person)
    print(j, "Добавлен новый пользователь", person)
    i += 1
    if i > 1:
        break

    


f = open("E:\\Gittext\\filtered_spisok.txt", 'w')
for line in filtered_list:
    f.write(line)
f.close()
print("\nДобавлено", i, "пользователей")



