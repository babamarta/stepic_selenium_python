from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    input3 = browser.find_element_by_xpath('//*[@id="book"]')
    input3.click()

    x = browser.find_element_by_xpath('//*[@id="input_value"]').text
    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    y = calc(x)
    input1.send_keys(y)
    input4 = browser.find_element_by_xpath('//*[@id="solve"]')
    input4.click()

finally:
    time.sleep(5)
    browser.quit()
