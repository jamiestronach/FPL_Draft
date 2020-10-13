from fixture_gen import Fixture_Generator
from main import league_data
import pandas as pd
from player import Player
from fixture import Fixture
from datetime import datetime as dt


class League():

    columns = ["Player_ID", "Player_Name", "Team_Name", "Wins", "Draws", "Losses", "GD", "Points"]

    def __init__(self, fixture_round):
        self.fixture_round = fixture_round
        self.league_table = self.final_table()
        self.order = ""

    def create_player_row(self, player_id):
        return [player_id, Player(player_id).name, Player(player_id).team_name, 0, 0, 0, 0, 0]

    def create_league_start(self, player_ids):
        league_lst = []

        for player in player_ids:
            league_lst.append(self.create_player_row(player))

        df = pd.DataFrame(data = league_lst, columns = self.columns)

        return df.set_index("Player_ID")

    def add_result(self, player_id, gameweek, fixture_set, league):
        result = Fixture(player_id, gameweek, fixture_set)
        
        league.at[player_id, "GD"] = league["GD"][player_id] + result.team_score
        
        if result.outcome_points == 3:
            league.at[player_id, "Wins"] = league["Wins"][player_id] + 1
            league.at[player_id, "Points"] = league["Points"][player_id] + 3

        elif result.outcome_points == 1:
            league.at[player_id, "Draws"] = league["Draws"][player_id] + 1
            league.at[player_id, "Points"] = league["Points"][player_id] + 1
        
        elif result.outcome_points == 0:
            league.at[player_id, "Losses"] = league["Losses"][player_id] + 1

        return league

    def add_results_player(self, player_id, fixture_set, league):
        
        for gameweek in range(league_data.last_active_gameweek):
            self.add_result(player_id, gameweek, fixture_set, league)
        
        return league

    def add_results_all_players(self, fixture_set, league):

        for player in list(fixture_set.keys()):
            self.add_results_player(player, fixture_set, league)
        
        return league

    def final_table(self):

        league = self.add_results_all_players(self.fixture_round, self.create_league_start(self.fixture_round.keys()))

        return league.sort_values(["Points", "GD"], ascending = False)




# start = dt.now()
# fixtures = Fixture_Generator(38606).get_fixtures()

# league = League().create_league_start(list(fixtures.keys()))

# print(Fixture(150578, 1, fixtures).outcome_points)
# print(League().add_result(150578, 1, fixtures, league))

# finish = dt.now()
# print(finish - start)



# start = dt.now()

# for i in range(5000):
#     fixtures = Fixture_Generator(90184).get_fixtures()
#     print(League(fixtures).league_table)

# finish = dt.now()

# print(finish - start)

