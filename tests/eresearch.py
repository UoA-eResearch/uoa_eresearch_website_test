from selenium import webdriver
from util import execute
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
    assert browser.find_element_by_partial_link_text('Faculty of Engineering')

  def test_for_broken_links(self):
    linkchecker_options = [
      "--check-extern", 
      "--no-warnings", 
      "--timeout 120",
      "--pause=3",
      "--ignore-url='.*eResearch-2013.pdf$'", 
      "--ignore-url='^http://www.jfsowa.com'",
    ]
    cmd = '''linkchecker %s %s''' % (' '.join(linkchecker_options), config.url)
    stdout, stderr, rc = execute(cmd, error_on_stderr=False, error_on_nonzero_rc=False)
    if rc > 0:
      print 'stdout:'
      print '#' * 80
      print stdout
      print '#' * 80
      print ''
      print 'stderr:'
      print '#' * 80
      print stderr
      print '#' * 80
    assert (rc == 0)

  @classmethod  
  def tearDownClass(cls):  
    config.driver.quit()

if __name__ == '__main__':
  unittest.main()
