from selenium import webdriver
import time
import math

try:
	br = webdriver.Chrome();
	lk = 'https://xn--80ab2ammfhls7c7be.xn--p1ai/'
#Автозаказ для быстрой кухни

finally:
	time.sleep(10)
	br.quit()