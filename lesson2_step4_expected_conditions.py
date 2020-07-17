from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element_by_css_selector("button.btn")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()

button1 = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button1.click()

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
#Вводим ответ в текстовое поле 
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)

button2 = browser.find_element_by_id("solve")
button2.click()
# ждем загрузки страницы
time.sleep(1)
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()