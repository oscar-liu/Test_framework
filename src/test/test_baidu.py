import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestBaiDu(unittest.TestCase):
    URL = 'http://www.baidu.com'
    on_path = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.dirname(on_path)
    base_path = os.path.dirname(src_path)
    driver_path = os.path.abspath(base_path+'/drivers/chromedriver')


    to_kw = (By.ID,'kw')
    to_su = (By.ID,'su')
    result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        print(self.to_kw)
        self.driver.find_element(*self.to_kw).send_keys('天气预报')
        self.driver.find_element(*self.to_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.result)
        for link in links:
            print(link.text)


    def test_search_1(self):
        self.driver.find_element(*self.to_kw).send_keys('Python selenium')
        self.driver.find_element(*self.to_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.result)
        for link in links:
            print(link.text)

if __name__ == '__main__':
    unittest.main()