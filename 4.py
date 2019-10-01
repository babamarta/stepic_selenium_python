from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element_by_xpath('//*[@id="treasure"]')
    x_element = x_element1.get_attribute("value")
    print(x_element)
    x = x_element
    y = calc(x)

    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    input1.send_keys(y)

    option1 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    option1.click()
    option2 = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    option2.click()
    option3 = browser.find_element_by_xpath('/html/body/div[1]/form/div/div/button')
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()