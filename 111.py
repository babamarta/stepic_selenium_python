from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("A")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("A")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("A")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("A")
    button = browser.find_element_by_xpath("//button[@type, 'submit' and text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла