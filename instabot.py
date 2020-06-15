from selenium import webdriver
import time
import accounts
all = 100

browser = webdriver.Chrome("E:\Gittext\chromedriver.exe")
browser.get("https://www.instagram.com/")



#Логинимся в инстаграм

browser.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(accounts.login)
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(accounts.password)
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[4]").click()
time.sleep(3)

# Подписчики Златана

browser.get("https://www.instagram.com/iamzlatanibrahimovic/")
time.sleep(2)
browser.find_element_by_xpath("//section/main/div/header/section/ul/li[2]/a").click()
time.sleep(2)
#element = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]") #Прокрутка через ползунок в окошке подписчиков ( 
# Сейчас исчез ползунок в самом окошке подписчиков )

#Прокрутка подписчиков

# browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" %6, element)
# time.sleep(0.7)
# browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" %4, element)
# time.sleep(0.7)
# browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" %3, element)
# time.sleep(0.7)
# browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" %2, element)
# time.sleep(0.7)
# browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" %1.3, element)
# time.sleep(0.7)

pers = []
t = 0.7
num_scroll = 0
p = 0 # коэфф ожидания 

while len(pers) < all:
    num_scroll += 1
    # browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)

    if num_scroll % 10 == 0:
        print("!")
        persons = browser.find_elements_by_xpath("//div[@role='dialog']/div[2]/ul/div/li/div/div/div/div/a[@title]")
        for i in range(len(persons)):
            pers.append(str(persons[i].get_attribute('href')))

    time.sleep(t)

    #ожидание
    if (len(pers) > (2000 + 1000*p) ):
        print("\ожидание 10 мин.")
        time.sleep(60*10)
        p += 1

# файл со списком пользователей
f = open("E:\Gittext\spisok.txt", 'w')
for person in pers:
    f.write(person)
    f.write("\n")
f.close()

browser.quit()
