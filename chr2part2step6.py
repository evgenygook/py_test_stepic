from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select #Подключил поиск по селекту

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	br = webdriver.Chrome();
	lk = 'http://SunInJuly.github.io/execute_script.html'		
	br.get(lk);


#собираю
	x = br.find_element_by_id('input_value').text
	radio_button = br.find_element_by_id('robotsRule')
	check_box = br.find_element_by_id('robotCheckbox')
	input_text = br.find_element_by_id('answer')
	btn = br.find_element_by_css_selector('button.btn')	

#раздаю
	answer = calc(x)
	check_box.click()
	br.execute_script("return arguments[0].scrollIntoView(true);",radio_button)
	radio_button.click()
	input_text.send_keys(answer)
	br.execute_script("return arguments[0].scrollIntoView(true);",btn)
	btn.click()

finally:
	time.sleep(10)
	br.quit()