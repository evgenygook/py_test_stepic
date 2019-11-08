from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select #Подключил поиск по селекту
import OS #подключил возможность работать с файлами


#file_path = os.path.join(current_dir, 'file.txt')
	br=webdriver.Chrome();
	lk='http://suninjuly.github.io/file_input.html'
	br.get(lk);

	#поиск

finally:
	time.sleep(10)
	br.quit()