from selenium import webdriver
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element_by_xpath('/html/body/form/div/div/button')
    element.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x)
    input3 = browser.find_element_by_xpath('//*[@id="answer"]')
    input3.send_keys(y)

    element = browser.find_element_by_xpath('/html/body/form/div/div/button')
    element.click()


finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()