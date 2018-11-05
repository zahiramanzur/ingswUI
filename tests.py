import os
import unittest
from selenium import webdriver
import pages


current_dir = os.path.abspath(os.path.dirname(__name__))

class FlightTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(os.path.join(current_dir, 'chromedriver'))
        self.base_url = 'http://newtours.demoaut.com'

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main(verbosity=2)
