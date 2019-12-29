from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):

 def test_abs1(self):

  link = "http://suninjuly.github.io/registration1.html"
  browser = webdriver.Chrome()
  browser.get(link)
  first_name = browser.find_element_by_xpath("//*[@placeholder='Input your first name']")
  last_name = browser.find_element_by_xpath("//*[@placeholder='Input your last name']")
  email = browser.find_element_by_xpath("//*[@placeholder='Input your email']")
  last_name.send_keys('Test_text')
  first_name.send_keys('Test_text')
  email.send_keys('Test_text')
  button = browser.find_element_by_css_selector("button.btn")
  button.click()
  time.sleep(1)
  welcome_text_elt = browser.find_element_by_tag_name("h1")
  welcome_text = welcome_text_elt.text
  self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

 def test_abs2(self):

  link = "http://suninjuly.github.io/registration2.html"
  browser = webdriver.Chrome()
  browser.get(link)
  first_name = browser.find_element_by_xpath("//*[@placeholder='Input your first name']")
  last_name = browser.find_element_by_xpath("//*[@placeholder='Input your last name']")
  email = browser.find_element_by_xpath("//*[@placeholder='Input your email']")
  last_name.send_keys('Test_text')
  first_name.send_keys('Test_text')
  email.send_keys('Test_text')
  button = browser.find_element_by_css_selector("button.btn")
  button.click()
  time.sleep(1)
  welcome_text_elt = browser.find_element_by_tag_name("h1")
  welcome_text = welcome_text_elt.text
  self.assertEqual(abs(-42), 42, "Should be absolute value of a number")  
        
if __name__ == "__main__":
    unittest.main()