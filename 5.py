from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    e = browser.find_element_by_id("num1").text
    r = browser.find_element_by_id("num2").text
    m = str(int(e) + int(r))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(m)
    option3 = browser.find_element_by_xpath('/html/body/div[1]/form/button')
    option3.click()






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()