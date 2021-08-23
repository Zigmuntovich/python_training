# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://itp-danfoss.web.app/")
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("s-k@ukr.net")
        driver.find_element_by_xpath("//input[@type='password']").click()
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("afpvfg2")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Забули пароль?'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("//textarea").click()
        driver.find_element_by_xpath("//textarea").click()
        driver.find_element_by_xpath("//textarea").clear()
        driver.find_element_by_xpath("//textarea").send_keys(u"Новий розрахунок 2")
        driver.find_element_by_xpath("//input").click()
        driver.find_element_by_xpath("//input").clear()
        driver.find_element_by_xpath("//input").send_keys("10")
        driver.find_element_by_xpath("//div[2]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[2]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[2]/div[2]/nz-input-number/div[2]/input").send_keys("3")
        driver.find_element_by_xpath("//div[3]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[3]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[3]/div[2]/nz-input-number/div[2]/input").send_keys("150")
        driver.find_element_by_xpath("//div[4]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[4]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[4]/div[2]/nz-input-number/div[2]/input").send_keys("70")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Тип системи:'])[1]/following::nz-select-top-control[1]").click()
        driver.find_element_by_xpath("//div[@id='cdk-overlay-0']/nz-option-container/div/cdk-virtual-scroll-viewport/div/nz-option-item/div").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)=concat('Тип під', \"'\", 'єднання:')])[1]/following::nz-select-top-control[1]").click()
        driver.find_element_by_xpath("//div[@id='cdk-overlay-1']/nz-option-container/div/cdk-virtual-scroll-viewport/div/nz-option-item/div").click()
        driver.find_element_by_xpath("//div[3]/div[2]/div[4]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[3]/div[2]/div[4]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[3]/div[2]/div[4]/div[2]/nz-input-number/div[2]/input").send_keys("300")
        driver.find_element_by_xpath("//div[5]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[5]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[5]/div[2]/nz-input-number/div[2]/input").send_keys("35")
        driver.find_element_by_xpath("//div[6]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[6]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[6]/div[2]/nz-input-number/div[2]/input").send_keys("90")
        driver.find_element_by_xpath("//div[7]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Номінальна температура в звороті (°C):'])[1]/following::button[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
