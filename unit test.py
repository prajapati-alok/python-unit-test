import unittest
from selenium import webdriver

class TestWebsiteLoad(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_website_load(self):
        self.driver.get("https://atg.world")
        self.assertIn("ATG", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
