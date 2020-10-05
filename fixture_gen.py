from pull_data import Pull_Data
import itertools

league_code = 38606


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

    def round_combinations(self):

        """Calculates all the combinations of games that could occur within a single gameweek. Ensures that each team only plays once, 
        and that each set of fixtures is unique. 

        Returns:
            list: Returns list of lists containing the fixtures, with each game indicated by paired ids within a single list. 
        """

        rounds = []

        for _round in itertools.combinations(self.different_game_coms(), int(self.num_players / 2)):

            duplicate_checker = []
            for team in _round:
                duplicate_checker += team
            if len(set(duplicate_checker)) == len(duplicate_checker):
                rounds.append(list(_round))

        return rounds


    # Full fixtures too ambitious for my computer by far in terms of CPU and time taken to work everything out. 
    # def full_fixture_cycle(self):

    #     fixtures = []

    #     for _cycle in itertools.combinations(self.different_round_coms(), int(self.num_players)):
    #         cycle = list(itertools.chain.from_iterable(_cycle))
    #         c = []
    #         for i in cycle:
    #             c.append(str(i[0]) + str(i[1]))
    #         print(len(set(c)))           
    #         if len(set(c)) == len(c):
    #             print(_cycle)
    #             fixtures.append(_cycle)
        
    #     return fixtures
    



print(Fixture_Generator().round_combinations())
# print(Fixture_Generator().full_fixture_cycle())



    
        




    






