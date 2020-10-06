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

    def team_fixtures_blank(self):

        team_fixtures = {}

        for team in self.player_id:
            team_fixtures[team] = [0] * (len(self.player_id) -1)
        
        return team_fixtures

    def played_in_gameweek(self):

        teams_left = {}

        for week in range(len(self.player_id)):
            teams_left[week] = self.player_id.copy()
    
        return teams_left

    def _remove_team_all_gameweeks(self, team, played_in_gameweek):

        for gameweek in range(len(played_in_gameweek.keys())):
            if team in played_in_gameweek[gameweek]:
                played_in_gameweek[gameweek].remove(team)

        return played_in_gameweek


    def team_fixtures(self):

        team_fixtures = self.team_fixtures_blank()
        teams = self.player_id
        played_in_gameweek = self.played_in_gameweek()

        for team in teams:

            played_in_gameweek = self._remove_team_all_gameweeks(team, played_in_gameweek)

            for gameweek, opponent in enumerate(team_fixtures[team]):
                
                if opponent == 0:

                    attempts = 0

                    while True:

                        game_opposition = random.choice(played_in_gameweek[gameweek])
                        
                        if game_opposition not in team_fixtures[team]:
                            team_fixtures[team][gameweek] = game_opposition
                            team_fixtures[game_opposition][gameweek] = team
                            played_in_gameweek[gameweek].remove(game_opposition)
                            break

                        if (len(played_in_gameweek[gameweek]) == 1) and (played_in_gameweek[gameweek] not in team_fixtures[team]):
                            return False

                        if attempts > 20:
                            return False
                        
                        attempts += 1

        return team_fixtures

    def get_result(self):

        while True:
            results = self.team_fixtures()
            if results:
                return results
                break

    def get_result_set(self, number):

        results = []

        for _results in range(number):
            results.append(self.get_result())

        return results

        

        



Fixture_Generator().get_result_set(1000)
        



        
