from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "https://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "input[type='text']")
    input1.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
