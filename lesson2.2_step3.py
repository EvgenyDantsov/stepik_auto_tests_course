from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/selects2.html"


def calc(x, z):
    return x + z


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    z_element = browser.find_element(By.ID, "num2")
    z = int(z_element.text)
    y = calc(x, z)
    browser.find_element(By.ID, "dropdown").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{y}']").click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
