from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/math.html"
	brws = webdriver.Chrome()
	brws.get(link)

#Окружение
	radio_button = brws.find_element_by_id('robotsRule')
	check_box = brws.find_element_by_id('robotCheckbox')
	x_element = brws.find_element_by_id('input_value')
	input_text = brws.find_element_by_id('answer')
	button = brws.find_element_by_css_selector('button.btn')

#предустановки
	x = x_element.text
	y = calc(x)

#действия
	check_box.click()
	radio_button.click()
	input_text.send_keys(y)
	button.click()
	
finally:
	time.sleep(10)
	brws.quit()