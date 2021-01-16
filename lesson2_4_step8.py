import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    #browser = webdriver.Firefox(executable_path="E:\WORK\PYTHON\practic\selenium\drivers\geckodriver.exe")
    browser = webdriver.Chrome("E:\WORK\PYTHON\practic\selenium\drivers\chromedriver.exe")
    browser.get(link)

    button = browser.find_element_by_css_selector("#book")

    heads = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    button.click()

    xel1 = browser.find_element_by_css_selector("#input_value")
    val = calc(xel1.text)
    print('val='+val)
    browser.find_element_by_css_selector("#answer").send_keys(val)

    button = browser.find_element_by_css_selector("#solve")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

except Exception as e:
    print("Ошибка", e)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()