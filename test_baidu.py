import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH
from utils.log import logger
from utils.file_read import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner

# print(DRIVER_PATH)
class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')

    excel = DATA_PATH + '/baidu.xlsx'

    on_path = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.dirname(on_path)
    base_path = os.path.dirname(src_path)


    to_kw = (By.ID,'kw')
    to_su = (By.ID,'su')
    result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    '''
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH+'/chromedriver')
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.to_kw).send_keys('天气预报')
        self.driver.find_element(*self.to_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.result)
        for link in links:
            # print(link.text)
            logger.info(link.text)

    '''

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH+'/chromedriver')
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()
    

    def test_excel_read_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.to_kw).send_keys(d['search'])
                self.driver.find_element(*self.to_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

    '''
    subTest是PY3 unittest里带的功能，PY2中没有，PY2中要想使用，需要用unittest2库。
    subTest是没有setUp和tearDown的，所以需要自己手动添加并执行。
    '''


if __name__ == '__main__':
    #报告
    report = REPORT_PATH + '/report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f , verbosity=2, title = "测试框架构建学习", description="HTML报告" )
        runner.run(TestBaiDu('test_excel_read_search'))

    #unittest.main()