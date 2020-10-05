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
                rounds.append(list(_round))

        return rounds

    def full_fixture_cycle(self):

        # fixtures = []

        # for _cycle in itertools.combinations(self.different_round_coms(), int(self.num_players)):

        #     cycle = list(itertools.chain.from_iterable(_cycle))
        #     c = []
        #     for i in cycle:
        #         c.append(str(i[0]) + str(i[1]))
        #         if set(c) == c:
        #             fixtures.append(cycle)
                
         
        #     return fixtures
        fixtures = []

        for _cycle in itertools.combinations(self.different_round_coms(), int(self.num_players)):
            cycle = list(itertools.chain.from_iterable(_cycle))
            c = []
            for i in cycle:
                c.append(str(i[0]) + str(i[1]))
                if len(set(c)) == len(c):
                    print(_cycle)
                    fixtures.append(_cycle)
        
        return fixtures



# print(Fixture_Generator().different_round_coms())
print(Fixture_Generator().full_fixture_cycle())



    
        




    






