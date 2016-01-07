from  selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):

 def setUp(self):
     self.driver =