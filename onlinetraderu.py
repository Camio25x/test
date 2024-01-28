# -*- coding: utf-8 -*-

from tabnanny import check
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


import time


service = Service('./geckodriver.exe')
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser = webdriver.Firefox(service=service, options=options)
browser.get("https://www.onlinetrade.ru")
browser.implicitly_wait(15)
time.sleep(30)

class TestKravchenko(unittest.TestCase):
    def test_auth(self):
        auth_buttons = browser.find_element(By.XPATH, "//a [@href='/member/login.html']")
        time.sleep(5)
        auth_buttons.click()
        time.sleep(5)
        username = browser.find_element(By.ID, "ajax_login_popup_email")
        username.clear()
        username.send_keys("nora26x@gmail.com")
        time.sleep(5)
        password = browser.find_element(By.ID, "ajax_login_popup_pass")
        password.clear()
        password.send_keys("89I726r415a")
        time.sleep(5)
        login_but = browser.find_element(By.NAME, "submit")
        time.sleep(5)
        login_but.click()
        
    def test_newCity(self):
       city = browser.find_element(By.XPATH, "//a [@class='ic__hasSet ic__hasSet__geo18x20 js__ajaxExchange']")
       time.sleep(5)
       city.click()
       selectNewCity = browser.find_element(By.XPATH, "//a [@href='/?c=72']")
       selectNewCity.click()
    
    def test_search(self):
        sear = browser.find_element(By.XPATH, "//input [@name='query']")
        sear.clear()
        sear.send_keys("Final Fantasy")    
        search_but = browser.find_element(By.XPATH, "//input [@class='header__search__inputGogogo']")
        search_but.click() 
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()
