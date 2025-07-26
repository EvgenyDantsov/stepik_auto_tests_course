from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

lable_price = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button=browser.find_element(By.ID, "book")
button.click()
# Решаем математическую задачу
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

# Вводим ответ
answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(y)
submit_button = browser.find_element(By.ID, "solve")
submit_button.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
