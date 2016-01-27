from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://live.guru99.com")

driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[4]/ul/li[1]/a").click()
#driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/div/div[1]/div[2]/a").click()
'''
for handle in driver.window_handles:
 driver.switch_to_window(handle)

 #driver.find_element_by_id("firstname").clear()
 #driver.find_element_by_id("firstname").send_keys("krishna")
 #driver.find_element_by_id("lastname").clear()
 #driver.find_element_by_id("lastname").send_keys("radha")
 #driver.find_element_by_id("email_address").clear()
 #driver.find_element_by_id("email_address").send_keys("radha@krishna.com")
 #driver.find_element_by_id("password").clear()
 #driver.find_element_by_id("password").send_keys("laxmana")
 #driver.find_element_by_id("confirmation").clear()
 #driver.find_element_by_id("confirmation").send_keys("laxmana")
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/div[2]/button").click()
'''


driver.find_element_by_id("email").send_keys("radha@krishna.com")
driver.find_element_by_id("pass").send_keys("laxmana")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/div/div[2]/div[2]/button").click()


X = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/p").text
print(X)
Y = "WELCOME, KRISHNA RADHA!"
print(Y)
if (X==Y):
    print("Registration is done")
else:
    print("Registration is not done")

driver.find_element_by_xpath("/html/body/div/div/header/div/div[3]/nav/ol/li[2]/a").click()
driver.find_element_by_class_name("link-wishlist").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/div[1]/form[1]/div/div/button[1]").click()

driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/form/div[1]/ul/li[1]/div/textarea").send_keys("laxmana@bwdc.in")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/form/div[1]/ul/li[2]/div/textarea").send_keys("Nice tv, picture quality")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/form/div[2]/button").click()

U = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/div[1]/ul/li/ul/li/span").text
print(U)
V = "Your Wishlist has been shared."
print(V)
if (U==V):
    print("Wishlist is shared successfully")
else:
    print("wishlist has not been shared successfully")


driver.close()
driver.quit()