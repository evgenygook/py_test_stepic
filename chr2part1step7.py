from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	br = webdriver.Chrome();
	lk = 'http://suninjuly.github.io/get_attribute.html'
	br.get(lk)

#собираю
	treasure=br.find_element_by_id('treasure')
	valuex = treasure.get_attribute('valuex')
	radio_button = br.find_element_by_id('robotsRule')
	check_box = br.find_element_by_id('robotCheckbox')
	input_text = br.find_element_by_id('answer')
	button = br.find_element_by_css_selector('button.btn')	
#раздаю
	answer = calc(valuex)
	check_box.click()
	radio_button.click()
	input_text.send_keys(answer)
	button.click()
	
finally:
	time.sleep(10)
	br.quit()