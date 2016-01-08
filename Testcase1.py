from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://live.guru99.com/")
try:
    assert 'Home page' in driver.title
    print('Assertion test pass')
except Exception as e:
    print('Assertion test failed',format(e))

elem = driver.find_element_by_xpath("/html/body/div/div/header/div/div[3]/nav/ol/li[1]/a").click()

try:
    assert 'Mobile' in driver.title
    print('Assertions test pass')
except Exception as e:
    print('Assertions test failed',format(e))
select = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/select/option[2]").click()





driver.close()
