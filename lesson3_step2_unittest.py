import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element_by_css_selector("div.form-group.first_class input:required")
        input1.send_keys("Olya")
        input2 = browser.find_element_by_css_selector("div.form-group.second_class input:required")
        input2.send_keys("Koskinen")
        input3 = browser.find_element_by_css_selector("div.form-group.third_class input:required")
        input3.send_keys("EMAIL")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element_by_css_selector("div.form-group.first_class input:required")
        input1.send_keys("Olya")
        input2 = browser.find_element_by_css_selector("div.form-group.second_class input:required")
        input2.send_keys("Koskinen")
        input3 = browser.find_element_by_css_selector("div.form-group.third_class input:required")
        input3.send_keys("EMAIL")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
if __name__ == "__main__":
    unittest.main()

