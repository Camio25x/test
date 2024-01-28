from os import system
from tabnanny import check
from typing import Self
import unittest
from unittest.case import _AssertRaisesContext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

import time


service = Service('./geckodriver.exe')
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser = webdriver.Firefox(service=service, options=options)
browser.get("https://the-internet.herokuapp.com")
browser.implicitly_wait(15)
time.sleep(5)

class TestKravchenko(unittest.TestCase):
    def test_addElement(self):
        time.sleep(5)
        testElem = browser.find_element(By.XPATH, "//a [@href='/add_remove_elements/']")
        testElem.click()
        time.sleep(5)
        add_but = browser.find_element(By.XPATH, "//button [@onclick='addElement()']")
        add_but.click()
        time.sleep(5)
        del_but = browser.find_element(By.XPATH, "//button [@onclick='deleteElement()']")
        del_but.click()
        try:
            browser.find_element(By.XPATH, "//button [@onclick='deleteElement()']")
        except NoSuchElementException:
            return False
        return True

    def test_check(self):
        browser.get("https://the-internet.herokuapp.com")
        browser.implicitly_wait(15)
        time.sleep(5)
        testElem = browser.find_element(By.XPATH, "//a [@href='/checkboxes']")
        testElem.click()
        time.sleep(5)
        check1 = browser.find_element(By.XPATH, ("//input [@type='checkbox']"))
        check1.click()
        if(check1.get_attribute("checked")) == "true":
            self.assertTrue((check1.get_attribute("checked") == "true"), "ok")
            time.sleep(5)
        else:
            self.assertTrue((check1.get_attribute("checked") != "true"), "Something went wrong")
            time.sleep(5)      
    
    def test_drop(self):
        browser.get("https://the-internet.herokuapp.com")
        browser.implicitly_wait(15)
        time.sleep(5)
        testElem = browser.find_element(By.XPATH, "//a [@href='/dropdown']")
        testElem.click()
        time.sleep(5)
        drop = browser.find_element(By.XPATH, ("//select [@id='dropdown']"))
        drop.click()
        time.sleep(5)
        sel = browser.find_element(By.XPATH, ("//option [@value='1']"))
        sel.click()
        if(sel.get_attribute("selected")) == "true":
            self.assertTrue((sel.get_attribute("selected") == "true"), "ok")
            time.sleep(5)
        else:
            self.assertTrue((sel.get_attribute("selected") != "true"), "Something went wrong")
            time.sleep(5)
         
    def test_auth(self):
        browser.get("https://the-internet.herokuapp.com")
        browser.implicitly_wait(15)
        time.sleep(5)
        testElem = browser.find_element(By.XPATH, "//a [@href='/login']")
        testElem.click()
        time.sleep(5)
        username = browser.find_element(By.ID, "username")
        username.clear()
        username.send_keys("tomsmith")
        time.sleep(5)
        password = browser.find_element(By.ID, "password")
        password.clear()
        password.send_keys("SuperSecretPassword!")
        time.sleep(5)
        login_but = browser.find_element(By.CLASS_NAME, "radius")
        time.sleep(5)
        login_but.click()
        URL = browser.current_url
        self.assertEqual(URL, "https://the-internet.herokuapp.com/secure" )
       
    def test_logOut(self):
        time.sleep(5)
        logout_but = browser.find_element(By.XPATH, "//a [@href='/logout']")
        time.sleep(5)
        logout_but.click()
        URL = browser.current_url
        self.assertEqual(URL, "https://the-internet.herokuapp.com/login" )

    def test_input(self):
        browser.get("https://the-internet.herokuapp.com")
        browser.implicitly_wait(15)
        time.sleep(5)
        testElem = browser.find_element(By.XPATH, "//a [@href='/key_presses']")
        testElem.click()
        time.sleep(5)
        input_text = browser.find_element(By.ID, "target")
        input_text.clear()
        input_text.send_keys("A")
        time.sleep(5)
        text_check = browser.find_element(By.ID, 'result').text
        self.assertEqual(text_check, "You entered: A" )
        
if __name__ == '__main__':
    unittest.main()
