from pull_data import Pull_Data
import itertools
import random

league_code = 38606


class Fixture_Generator():

    def __init__(self, league_code=league_code):
        self.num_players = int(Pull_Data(league_code=league_code).get_number_players())
        self.player_id = list(Pull_Data(league_code=league_code).get_player_names())

    
    def game_combinations(self):

        """Calculates all the possible combinations of games, with each team playing each other only once. Orders the each fixture so the side 
        with the highest id is the first number.

        Returns:
            list: contains list of all the game combinations for a given number of fixtures. 
        """

        fixtures = []
        iter_list = itertools.combinations(self.player_id, 2)

        for fix in iter_list:
            fixtures.append([max(fix), min(fix)])

        return fixtures

    def round_combinations(self):

        """Calculates all the combinations of games that could occur within a single gameweek. Ensures that each team only plays once, 
        and that each set of fixtures is unique. 

        Returns:
            list: Returns nested lists containing the fixtures. Each initial list contains a group of fixtures, with each list inside that containing
            paired team ids for individual games. 
        """

        rounds = []

        for _round in itertools.combinations(self.game_combinations(), int(self.num_players / 2)):

            duplicate_checker = []
            for team in _round:
                duplicate_checker += team
            if len(set(duplicate_checker)) == len(duplicate_checker):
                rounds.append(list(_round))

        return rounds

    def round_combinations_combined(self):
        
        return [[str(team[0]) + str(team[1]) for team in games] for games in self.round_combinations()]

    def random_combinations(self):
        
        fixtures = []
        games_played = []

        combinations = self.round_combinations_combined()
        
        while len(fixtures) <= (len(combinations[0]) * 2) -1:
            _round = random.choice(combinations)
            non_duplicates = 0
            for game in _round:
                
                if game in games_played:                   
                    break
                else:
                    games_played.append(game)
                    non_duplicates += 1
                    if non_duplicates == (len(combinations[0])):
                        combinations = [theround for theround in combinations if game not in theround]
                        fixtures.append(_round)
                        

    

        return fixtures



        

    



# print(Fixture_Generator().round_combinations_combined())

print(Fixture_Generator().random_combinations())
# print(len(Fixture_Generator().game_combinations()))


# print(len(Fixture_Generator().round_combinations_combined()))

# new_list = [games for games in Fixture_Generator().round_combinations_combined()]

# print(new_list)
# 150642150578

# print(len([game for game in Fixture_Generator().round_combinations_combined() if "150642150578" not in game]))