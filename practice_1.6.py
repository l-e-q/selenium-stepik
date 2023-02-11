from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = " http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.XPATH, "//input[@placeholder = 'Input your first name']").send_keys('Don')
    browser.find_element(By.XPATH, "//input[@placeholder = 'Input your last name']").send_keys('Yagon')
    browser.find_element(By.XPATH, "//input[@placeholder = 'Input your email']").send_keys('just_mail')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()