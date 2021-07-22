from flask import Flask
import unittest, sys

sys.path.append('../QuickASL') # imports python file from parent directory
from main import app #imports flask app object

class page_loading_tests(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_learn_more_page(self):
        response = self.app.get('/learn-more', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_main_page(self):
        response = self.app.get('/main_page', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
#     def test_clear_page(self):
#         response = self.app.get('/clear_images', follow_redirects=True)
#         self.assertEqual(response.status_code, 200)
#     def test_clear_page(self):
#         response = self.app.get('/process_query', follow_redirects=True)
#         self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()