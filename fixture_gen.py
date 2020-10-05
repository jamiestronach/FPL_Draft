from pull_data import Pull_Data
import itertools

league_code = 90184


class Fixture_Generator():

    def __init__(self, league_code=league_code):
        self.num_players = int(Pull_Data(league_code=league_code).get_number_players())
        self.player_id = list(Pull_Data(league_code=league_code).get_player_names())

    
    def different_game_coms(self):

        fixtures = []
        iter_list = itertools.combinations(self.player_id, 2)

        for fix in iter_list:
            fixtures.append([max(fix), min(fix)])

        return fixtures

    def different_round_coms(self):

        rounds = []

        for _round in itertools.combinations(self.different_game_coms(), int(self.num_players / 2)):
            r = []
            for i in _round:
                r += i
            if len(set(r)) == len(r):
                rounds.append(_round)

        return rounds




print(len(Fixture_Generator().different_round_coms()))

    
        




    






