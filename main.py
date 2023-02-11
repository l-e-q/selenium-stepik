from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
import math


def calc(alpha):
    return str(math.log(abs(12 * math.sin(int(alpha)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()
    x = calc(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(x)
    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(5)
    browser.quit()
