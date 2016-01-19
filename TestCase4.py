from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://live.guru99.com/")

driver.find_element_by_class_name("level0").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[3]/div/div[3]/ul/li[2]/a").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/div/div[3]/ul/li[2]/a").click()
driver.find_element_by_css_selector("html#top.js.no-touch.localstorage.no-ios body.catalog-category-view.categorypath-mobile-html.category-mobile div.wrapper div.page div.main-container.col3-layout div.main div.col-right.sidebar div.block.block-list.block-compare div.block-content div.actions button.button").click()

# Window handling
for handle in driver.window_handles:
    driver.switch_to_window(handle)
A = driver.find_element_by_xpath("/html/body/div/div[1]/h1").text
#print(A)
B = "COMPARE PRODUCTS"
#print(B)
if A==B:
    print("compare products page is opened")
else:
    print("compare products page is not opened")

I = driver.find_element_by_xpath("/html/body/div/table/tbody[1]/tr[1]/td[1]/h2/a").text
#print(I)
J = "SONY XPERIA"
#print(J)
if I==J:
    print("Sony Xperia mobile is reflected")
else:
    print("Sony Xperia mobile is not reflected")

M = driver.find_element_by_xpath("/html/body/div/table/tbody[1]/tr[1]/td[2]/h2/a").text
#print(M)
N = "IPHONE"
#print(N)
if M==N:
    print("IPhone is reflected")
else:
    print("IPhone is not reflected")
driver.close()
print("Pop-Window is Closed")

for handle in driver.window_handles:
    driver.switch_to_window(handle)
print(driver.title)









