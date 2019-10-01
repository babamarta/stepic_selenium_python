from selenium import webdriver
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element_by_xpath('/html/body/div[1]/form/div/input[1]')
    option1.send_keys("A")
    option2 = browser.find_element_by_xpath('/html/body/div[1]/form/div/input[2]')
    option2.send_keys("AQ")
    option3 = browser.find_element_by_xpath('/html/body/div[1]/form/div/input[3]')
    option3.send_keys("AQa")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'hw.txt')  # добавляем к этому пути имя файла
    option4 = browser.find_element_by_xpath('//*[@id="file"]')
    option4.send_keys(file_path)

    element = browser.find_element_by_xpath('/html/body/div[1]/form/button')
    element.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()