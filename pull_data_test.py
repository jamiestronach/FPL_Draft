import unittest
from pull_data import Pull_Data

league_code = 3860643096935673046340967

class TestPull_Data(unittest.TestCase):

    def test_get_response(self):
        self.assertTrue(Pull_Data(league_code=league_code).get_response().ok)



if __name__ == '__main__' :
    unittest.main()