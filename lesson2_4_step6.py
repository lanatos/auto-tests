from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/cats.html"
    #browser = webdriver.Firefox(executable_path="E:\WORK\PYTHON\practic\selenium\drivers\geckodriver.exe")
    browser = webdriver.Chrome("E:\WORK\PYTHON\practic\selenium\drivers\chromedriver.exe")
    browser.get(link)

    browser.find_element_by_id("button") 

except Exception as e:
    print("Ошибка", e)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()