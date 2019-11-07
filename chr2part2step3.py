from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select #Подключил поиск по селекту

try:
	br = webdriver.Chrome();
	lk = 'http://suninjuly.github.io/selects1.html'
	br.get(lk);

#собираю
	select = Select(br.find_element_by_tag_name("select")) #записываю в функцию дропдовн
	num1=br.find_element_by_id('num1').text
	num2=br.find_element_by_id('num2').text

	dropdown = br.find_element_by_id('dropdown')
	button = br.find_element_by_css_selector('button.btn')
#раздаю
	dropdown.click()
	summ=str(int(num1)+int(num2))


	srch = select.select_by_visible_text(summ)
	button.click()


finally:
	time.sleep(10)
	br.quit()