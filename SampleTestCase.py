from selenium import  webdriver
from  selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.akamai.com/")

try:
    assert "Content Delivery Network (CDN) & Cloud Computing Services | Akamai" in driver.title
    print('Test pass')
except Exception as e:
    print('Test fail',format(e))

elem = driver.find_element_by_css_selector("html#nav.js.cssanimations.flexbox.csspointerevents.csspositionsticky.csstransforms.supports.csstransforms3d.csstransitions.no-pointerevents.svg.checked.target.wf-active body div#main.page-wrapper--outer header.global-header div.primary-nav__outer-wrapper.outer-wrapper div.primary-nav__inner-wrapper.inner-wrapper nav.primary-nav ul.primary-nav__level-one.tabs.tabs__tab-length--7 li.tabs__single-tab.tab.tab--4 a.gtm_MegaMenu_Nav").click()
elem = driver.find_element_by_xpath("/html/body/div[1]/ul/li[1]/label").click()
elem = driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div/nav/ul/li[6]/a").click()
select = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section[1]/div/div/div/form/div[2]/fieldset[1]/select/option[4]").click()
select = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section[1]/div/div/div/form/div[2]/fieldset[2]/select/option[4]").click()
select = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section[1]/div/div/div/form/div[2]/fieldset[3]/select/option[2]").click()



driver.close()