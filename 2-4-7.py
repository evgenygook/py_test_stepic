from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
try:
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
	button = browser.find_element_by_id("book")
	button.click()

	browser.execute_script("arguments[0].scrollIntoView();", browser.find_element_by_css_selector('#input_value'))
	number = browser.find_element_by_css_selector('#input_value').text
	answer = browser.find_element_by_css_selector('#answer')
	answer.send_keys(calc(number))
	submit = browser.find_element_by_css_selector('#solve')
	submit.click()

finally:
	time.sleep(10)
	browser.quit()