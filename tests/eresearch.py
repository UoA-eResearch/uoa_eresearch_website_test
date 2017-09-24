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
    browser.find_element_by_partial_link_text('Research collaboration').click() 
    #browser.switch_to_frame(0)
    assert browser.find_element_by_partial_link_text('Faculty of Arts')
    assert browser.find_element_by_partial_link_text('Faculty of Science')
    assert browser.find_element_by_partial_link_text('Faculty of Engineering')

  def test_for_broken_links(self):
    linkchecker_options = [
      "--check-extern", 
      "--no-warnings", 
      "--timeout 90",
      "--pause=3",
      "--ignore-url='.*eResearch-2013.pdf$'", 
      "--ignore-url='^http://www.jfsowa.com'",
      "--ignore-url='^https://platforms.monash.edu/eresearch/*'",
      "--ignore-url='^http://brain.oxfordjournals.org/content/130/9/2327.full'",
      "--ignore-url='^https://www.auckland.ac.nz/en/about/the-university/atoz-directory.html'",
      "--ignore-url='^https://www.auckland.ac.nz/en/admin/access-links/directory.html'",
      "--ignore-url='^https://www.auckland.ac.nz/en/admin/quick-links/a-to-z-directory.html'",
    ]
    cmd = '''linkchecker %s %s''' % (' '.join(linkchecker_options), config.url)
    print("%s" % cmd)
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
