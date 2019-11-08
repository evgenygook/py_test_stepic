from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select #Подключил поиск по селекту
import os #подключил возможность работать с файлами


#file_path = os.path.join(current_dir, 'file.txt')
try:
	br = webdriver.Chrome();
	lk ='http://suninjuly.github.io/file_input.html'
	br.get(lk);

	#поиск
	current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'fish_text.txt') #загружаю файл. Он находится в папке с тестом
	f_name = br.find_element_by_css_selector(".form-control[placeholder='Enter first name']")
	l_name = br.find_element_by_css_selector(".form-control[placeholder='Enter last name']")
	email = br.find_element_by_css_selector(".form-control[placeholder='Enter email']")
	file = br.find_element_by_id('file')
	btn = br.find_element_by_css_selector('button.btn')	

	#действия
	f_name.send_keys("First name")
	l_name.send_keys("Last Name")
	email.send_keys("test@my.py")
	file.send_keys(file_path)
	btn.click()


finally:
	time.sleep(10)
	br.quit()