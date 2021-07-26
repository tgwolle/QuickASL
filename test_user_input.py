from flask import Flask
import unittest, sys
from main import get_input


sys.path.append('../QuickASL') # imports python file from parent directory
from main import app #imports flask app object

class TestFileName(unittest.TestCase):
  # executed prior to each test run
    def setUp(self):
        self.app = app.test_client()

    def test_get_input(self):
        self.assertNotEqual(get_input(), None)
        
if __name__ == '__main__':
    unittest.main()