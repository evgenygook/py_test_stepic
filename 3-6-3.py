import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.mark.parametrize('number', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    area =  browser.find_element_by_css_selector(".textarea")
    answer = math.log(int(time.time()))
    area.send_keys(str(answer))
    print(answer)
    btn = browser.find_element_by_css_selector(".submit-submission")
    btn.click()
    msg = browser.find_element_by_css_selector(".smart-hints__hint").text
    print(msg)
    assert msg == "Correct!"
 