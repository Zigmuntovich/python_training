# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from data_class import Data

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_danfoss_itp(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, user_email="s-k@ukr.net", password="afpvfg2")
        self.fill_data(driver, Data(p1=10, p2=3, t1=150, t2=70, heat_power=300, static_height=35, t11=90))
        driver.find_element_by_xpath("//button/*[text()='Розрахунок']/..").click()

    def fill_data(self, driver, data: Data):
        driver.find_element_by_xpath("//textarea").click()
        driver.find_element_by_xpath("//textarea").clear()
        driver.find_element_by_xpath("//textarea").send_keys(u"Новий розрахунок 2")
        driver.find_element_by_xpath("//input").click()
        driver.find_element_by_xpath("//input").clear()
        driver.find_element_by_xpath("//input").send_keys(data.p1)
        driver.find_element_by_xpath("//div[2]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[2]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[2]/div[2]/nz-input-number/div[2]/input").send_keys(data.p2)
        driver.find_element_by_xpath("//div[3]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[3]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[3]/div[2]/nz-input-number/div[2]/input").send_keys(data.t1)
        driver.find_element_by_xpath("//div[4]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[4]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[4]/div[2]/nz-input-number/div[2]/input").send_keys(data.t2)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Тип системи:'])[1]/following::nz-select-top-control[1]").click()
        driver.find_element_by_xpath(
            "//div[@id='cdk-overlay-0']/nz-option-container/div/cdk-virtual-scroll-viewport/div/nz-option-item/div").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)=concat('Тип під', \"'\", 'єднання:')])[1]/following::nz-select-top-control[1]").click()
        driver.find_element_by_xpath(
            "//div[@id='cdk-overlay-1']/nz-option-container/div/cdk-virtual-scroll-viewport/div/nz-option-item/div").click()
        driver.find_element_by_xpath("//div[3]/div[2]/div[4]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[3]/div[2]/div[4]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[3]/div[2]/div[4]/div[2]/nz-input-number/div[2]/input").send_keys(data.heat_power)
        driver.find_element_by_xpath("//div[5]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[5]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[5]/div[2]/nz-input-number/div[2]/input").send_keys(data.static_height)
        driver.find_element_by_xpath("//div[6]/div[2]/nz-input-number/div[2]/input").click()
        driver.find_element_by_xpath("//div[6]/div[2]/nz-input-number/div[2]/input").clear()
        driver.find_element_by_xpath("//div[6]/div[2]/nz-input-number/div[2]/input").send_keys(data.t11)

    def login(self, driver, user_email, password):
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(user_email)
        driver.find_element_by_xpath("//input[@type='password']").click()
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Забули пароль?'])[1]/following::button[1]").click()

    def open_home_page(self, driver):
        driver.get("https://itp-danfoss.web.app/")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
