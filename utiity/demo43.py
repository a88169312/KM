import unittest

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class PythonSearch(unittest.TestCase):
    def setUp(self):
        #print("prepare some data...")
        opts = Options()
        opts.headless = True
        assert  opts.headless
        #self.browser = Chrome(options=opts)
        self.browser = Chrome()
    def tearDown(self):
        print("store and clean space...")
    def test1(self):
        #print("exec test 1")
        browser = self.browser
        browser.get("https://www.python.org")
        element = browser.find_element_by_name('q')
        element.clear()
        element.send_keys("too")
        #element.send_keys("toogd")
        element.send_keys(Keys.RETURN)
        assert "No results found" not in browser.page_source
        pass

    #@unittest.skip("not yet implement")
    def testabc(self):
        print("exec test abc")
        pass
#if __name__ == '__main__':
#    unittest.main()