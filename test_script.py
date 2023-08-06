"""
Python script that uses the Selenium WebDriver library to perform automated testing on a given URL. 
The script is structured as a test case class that inherits from the unittest.TestCase class, 
which provides a framework for organizing and running test cases.

unittest: A built-in Python library for creating and running unit tests.
selenium.webdriver: The Selenium WebDriver library, which allows interaction with web browsers.
selenium.common.exceptions.NoSuchElementException: An exception class for handling cases where a web element is not found.

Defining the Test Class:
The test class is named TestTemplate and inherits from unittest.TestCase.
A docstring is provided to describe the purpose of the class.
Setting Up the Test Environment:

The setUp method is called before each test case starts. 
It sets up the web driver configuration for running tests.
It creates a Chrome WebDriver instance with specific options using webdriver.ChromeOptions().
The Chrome options are set to run the browser in headless mode, which means the browser will not be displayed during testing.
The implicitly_wait(10) method is used to set an implicit wait time of 10 seconds. 
This means the driver will wait up to 10 seconds for the web elements to be available before raising an exception.
The tearDown method is called after each test case finishes, and it stops the web driver.

Test Case:
The test_case_1 method is a test case that will be executed by the test runner.
It is decorated with a docstring to describe the purpose of the test case.
The test case navigates to the URL "https://www.caru-care.com/" using self.driver.get().
It then attempts to find and click an element with the class name "desctop-menu-large" using self.driver.find_element().
If the element is not found, the test case will fail and raise a NoSuchElementException.

Main Execution:
The if __name__ == '__main__': block is the entry point for executing the script.
The test suite is created using unittest.TestLoader().loadTestsFromTestCase(TestTemplate).
The test suite is then run using unittest.TextTestRunner(verbosity=2).run(suite). 
The verbosity=2 argument means that more detailed output will be displayed during test execution.

This script defines a single test case that navigates to "https://www.caru-care.com/" and 
attempts to click on an element with the class name "desctop-menu-large" on that page. 
If the element is found and clicked successfully, the test case passes.
Otherwise, it will fail with a NoSuchElementException. The test is performed using the Chrome WebDriver in headless mode.
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
        """Find and click top menu element on caru-care.com"""
        try:
            self.driver.get('https://www.caru-care.com/')
            el = self.driver.find_element(By.CLASS_NAME, 'desctop-menu-large')
            el.click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
