#! /usr/bin/python3

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://accounts.google.com/')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('aleksandar@greater.nl')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('@Sammas011')
passwordElem.submit()
