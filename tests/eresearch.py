from selenium import webdriver
import unittest
import config
import time

class EresearchTests(unittest.TestCase):

  @classmethod  
  def setUpClass(cls):  
    config.driver = eval(config.driver)

  def test_projects_iframe(self):
    browser = config.driver
    browser.get(config.url)
    browser.find_element_by_partial_link_text('Projects and research outcomes').click() 
    browser.find_element_by_partial_link_text('Current projects and research outcomes').click() 
    browser.switch_to_frame(0)
    assert browser.find_element_by_partial_link_text('Landcare Research')
    assert browser.find_element_by_partial_link_text('University of Otago')
    assert browser.find_element_by_partial_link_text('University of Auckland')
    assert browser.find_element_by_partial_link_text('Faculty of Science')
    assert browser.find_element_by_partial_link_text('Facult of Engineering')

  @classmethod  
  def tearDownClass(cls):  
    config.driver.close()

if __name__ == '__main__':
  unittest.main()
