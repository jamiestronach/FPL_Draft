from fixture_gen import Fixture_Generator
import unittest

single_set = Fixture_Generator().get_result()
key = list(single_set.keys())

class Test_Fixture_Test(unittest.TestCase):  

    def test_check_each_team_plays_once(self):

        self.assertEqual(len(set(single_set[key[0]])), len(single_set[key[0]]))
        self.assertEqual(len(set(single_set[key[1]])), len(single_set[key[1]]))
        self.assertEqual(len(set(single_set[key[1]])), len(single_set[key[0]]))

    def played_once_per_GW(self, gameweek):

        teams_played = []
        
        for team in key:
            teams_played.append(single_set[team][gameweek])

        return sorted(teams_played)

    def test_check_each_gameweek(self):

        self.assertEqual(self.played_once_per_GW(1), sorted(key))
        self.assertEqual(self.played_once_per_GW(0), sorted(key))
 





if __name__ == '__main__' :
    unittest.main()
