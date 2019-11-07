from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Окружение
    first_name = browser.find_element_by_xpath("//*[@placeholder='Input your first name']")
    last_name = browser.find_element_by_xpath("//*[@placeholder='Input your last name']")
    email = browser.find_element_by_xpath("//*[@placeholder='Input your email']")
    
    #действия
    last_name.send_keys('Test_text')
    first_name.send_keys('Test_text')
    email.send_keys('Test_text')
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)
    browser.quit()
