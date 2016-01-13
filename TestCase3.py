from  selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://live.guru99.com/")
driver.find_element_by_class_name("level0 ").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[2]/div/div[3]/button").click()
A= driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/table/tbody/tr/td[4]/input")
A.clear()
A.send_keys("1000")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/table/tbody/tr/td[4]/button").click()
B= driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/ul/li/ul/li/span").text
#print(B)
if 'Some of the products cannot be ordered in requested quantity.' == B:
    print("Error msg is verified")
else:
    print("Error msg is not verified")

driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/table/tfoot/tr/td/button[2]/span/span").click()
C= driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[1]/h1").text
#print(C)
if 'SHOPPING CART IS EMPTY' == C:
    print("Cart is Empty")
else:
    print("Cart is not Empty")
driver.close()
driver.quit()