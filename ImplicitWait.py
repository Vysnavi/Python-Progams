from  selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.akamai.com/")
main = driver.find_element_by_id("main")
