from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	br = webdriver.Chrome();
	lk ='http://suninjuly.github.io/alert_accept.html'
	br.get(lk);

	btn = br.find_element_by_css_selector('.btn.btn-primary').click()
	alert = br.switch_to.alert.accept()
	number = br.find_element_by_css_selector('#input_value').text
	answer = br.find_element_by_css_selector('#answer')
	answer.send_keys(calc(number))
	submit = br.find_element_by_css_selector('.btn.btn-primary').click()

finally:
	time.sleep(10)
	br.quit()