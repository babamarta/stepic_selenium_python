from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_xpath('//*[@id="input_value"]').text
    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    y = calc(x)
    input1.send_keys(y)


    option1 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    option1.click()
    option2 = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    option3 = browser.find_element_by_xpath('/html/body/div[1]/form/button')
    option3.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()