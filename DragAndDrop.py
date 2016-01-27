from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class DragAndDrop():

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://www.bwdc.in")
    