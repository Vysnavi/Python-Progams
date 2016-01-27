from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://live.guru99.com")

driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[4]/ul/li/a").click()
driver.find_element_by_id("email").send_keys("radha@krishna.com")
driver.find_element_by_id("pass").send_keys("laxmana")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/div/div[2]/div[2]/button").click()


driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div[2]/ul/li[8]/a").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/div[1]/form[1]/div/table/tbody/tr/td[5]/div/button").click()

driver.find_element_by_id("country").send_keys("United States")
driver.find_element_by_id("region_id").send_keys("New York")
driver.find_element_by_id("postcode").send_keys("543251")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/div/form/div/button").click()


S = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/div/form[2]/dl/dd/ul/li/label/span").text
T ="$5.00"
if( S ==T):
    print("shipping cost is generated")
else:
    print("shipping cost is not generated")

driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/div/form[2]/div/button").click()

U = driver.find_element_by_xpath("//html/body/div/div/div[2]/div/div/div/div[3]/div/table/tfoot/tr/td[2]/strong/span").text
print(U)
V ="$620.00"
if (U ==V):
    print("SHIPPING COST IS ADDED TO THE TOTAL")
else:
    print("SHIPPING COST IS  NOT ADDED TO THE TOTAL")

driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[3]/div/ul/li[1]/button") .click()
driver.find_element_by_id("billing:firstname").clear()
driver.find_element_by_id("billing:lastname").clear()



driver.find_element_by_id("billing:street1").clear()
driver.find_element_by_id("billing:street1").send_keys("148 crown street")
driver.find_element_by_id("billing:city").clear()
driver.find_element_by_id("billing:city").send_keys("New York")
driver.find_element_by_id("billing:region_id").clear()
driver.find_element_by_id("billing:region_id").send_keys("New York")

driver.find_element_by_id("billing:postcode").clear()
driver.find_element_by_id("billing:postcode").send_keys(2000)
#driver.find_element_by_id("billing:country_id").clear()
#driver.find_element_by_id("billing:country_id").send_keys("United States")
driver.find_element_by_id("billing:telephone").clear()
driver.find_element_by_id("billing:telephone").send_keys(88906754)


driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/ol/li[1]/div[2]/form/div/div/button").click()







