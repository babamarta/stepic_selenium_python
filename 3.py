from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    input1.send_keys(y)

    option1 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    option1.click()
    option2 = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    option2.click()
    option3 = browser.find_element_by_xpath('/html/body/div[1]/form/button')
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()