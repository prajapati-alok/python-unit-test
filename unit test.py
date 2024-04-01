import unittest
from selenium import webdriver

class TestWebsiteLoad(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver (assuming Chrome here)
        self.driver = webdriver.Chrome()

    def test_website_load(self):
        # Open the website
        self.driver.get("https://atg.world")
        # Check if "ATG" is present in the title
        self.assertIn("ATG", self.driver.title)

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
