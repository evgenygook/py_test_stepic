from selenium import webdriver
import time
import math

try: 
	brws = webdriver.Chrome();
	lnk = 'http://suninjuly.github.io/selects1.html'
	brws.get(lnk)
	
#Элементы окружения	
	x = brws.find_element(By.ID, 'num1').text
	y = brws.find_element(By.ID, 'Num2').text
	dropdown = brws.find_element(By.CLASS, 'custom-select')
	num1 = int(x)
	num2 = int(y)
#действия
 	summy = (num1+num2)
 	dropdown.click()
 	option = brws.find_element(By.CSS,'[value='summy']')
 	option.click()
	
finally:
time.sleep(10)
brws.quit()