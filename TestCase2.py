import unittest
from selenium import webdriver


class Testcase2 (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_sample_in_Test_Case2(self):
        driver = self.driver
        driver.get("http://live.guru99.com")
        driver.find_element_by_class_name("level0 ").click()
        X = '$100.00'
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[3]/div/h2/a").click()
        Y = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/form/div[3]/div[2]/div/span/span").text
        print(Y)

        if X == Y:
            print("Price of sony xperia is same")
        else:
            print("Price of sony xperia is not same")



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

