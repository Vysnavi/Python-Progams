from  selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://live.guru99.com/")
driver.find_element_by_class_name("level0 ").click()
a = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[2]/div/div[1]/span/span").text
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[2]/a/img").click()
b = driver.find_element_by_class_name("price").text
if(a==b):
    print("both values are equal")
else:
    print("Both values are not equal")

driver.close()