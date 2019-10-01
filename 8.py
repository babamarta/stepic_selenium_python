from selenium import webdriver
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element_by_xpath('/html/body/form/div/div/button')
    element.click()
    confirm = browser.switch_to.alert
    confirm.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x)

    input3 = browser.find_element_by_xpath('//*[@id="answer"]')
    input3.send_keys(y)






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()