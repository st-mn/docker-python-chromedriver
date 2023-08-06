"""
A simple selenium test example written by python
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Find and click top-left element CARU logo tt-obj-logo"""
        try:
            self.driver.get('https://www.caru-care.com/')
            el = self.driver.find_element(By.CLASS_NAME, 'shopify-selection')
            el.click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case_2(self):
        """Find and click top-right element CARU menu tt-obj-options"""
        try:
            self.driver.get('https://www.caru-care.com/')
            el = self.driver.find_element(By.CLASS_NAME, 'tt-col-obj tt-obj-options')
            el.click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
