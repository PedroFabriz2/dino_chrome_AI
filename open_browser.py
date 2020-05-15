from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

with webdriver.Chrome("/Users/fabriz_pedro/py_projects/redes_neurais/dino/chromedriver") as driver: 
	
	driver.get("https://www.google.com.br/")
	time.sleep(2)
	element = driver.find_element_by_tag_name('body')
	element.send_keys(Keys.ARROW_UP)	

	# while(True):
	# 	#here goes the AI script, but for now...
	# 	element.send_keys(Keys.ARROW_UP)		

	


	


