import unittest
from pull_data import Pull_Data
import json

league_code = 38606

class TestPull_Data(unittest.TestCase):

    def test_get_response(self):
        self.assertTrue(Pull_Data(league_code=league_code).get_response().ok)

    def test_json(self):
        # Checking the response object has been correctly formatted as a json
        self.assertIsInstance(Pull_Data(league_code=league_code).get_json(), dict)
        # Checking that league entries is one of the keys in the dictionary
        self.assertIn('league_entries', Pull_Data(league_code=league_code).get_json().keys())
        # Checking that 
        self.assertGreater(Pull_Data(league_code=league_code).number_players(), 11)
        


if __name__ == '__main__' :
    unittest.main()