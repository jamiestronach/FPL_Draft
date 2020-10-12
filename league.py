from fixture_gen import Fixture_Generator
import pandas as pd
from player import Player
from fixture import Fixture
from datetime import datetime as dt


class League():

    columns = ["Player_ID", "Player_Name", "Team_Name", "Wins", "Draws", "Losses", "GD", "Points"]

    def __init__(self, fixture_round = None):
        self.league_table = ""
        self.fixture_round = ""
        self.order = ""

    def create_player_row(self, player_id):
        return [player_id, Player(player_id).name, Player(player_id).team_name, 0, 0, 0, 0, 0]

    def create_league_start(self, player_ids):
        league_lst = []

        for player in player_ids:
            league_lst.append(self.create_player_row(player))

        df = pd.DataFrame(data = league_lst, columns = self.columns)

        return df.set_index("Player_ID")

    def add_result(self, team, gameweek, fixture_set, league):
        result = Fixture(team, gameweek, fixture_set)
        
        league.at[team, "GD"] = league["GD"][team] + result.team_score
        
        if result.outcome_points == 3:
            league.at[team, "Wins"] = league["Wins"][team] + 1
            league.at[team, "Points"] = league["Points"][team] + 3

        elif result.outcome_points == 1:
            league.at[team, "Draws"] = league["Draws"][team] + 1
            league.at[team, "Points"] = league["Points"][team] + 1
        
        elif result.outcome_points == 0:
            league.at[team, "Losses"] = league["Losses"][team] + 1

        return league

    def add_results_player(self):

        pass



    
    

    def loop_results(self):
        pass



start = dt.now()
# print(list(Fixture_Generator(38606).get_fixtures().keys()))
fixtures = Fixture_Generator(38606).get_fixtures()

league = League().create_league_start(list(fixtures.keys()))

# # print(league)
print(Fixture(150578, 1, fixtures).outcome_points)
print(League().add_result(150578, 1, fixtures, league))

finish = dt.now()
print(finish - start)
