from fixture_gen import Fixture_Generator
import pandas as pd
from player import Player


class League():

    columns = ["Player_Name", "Team_Name", "Wins", "Draws", "Losses", "GD", "Points"]

    def __init__(self, fixture_round):
        self.league_table = ""
        self.fixture_round = ""
        self.order = ""

    def create_player_row(self, player_id):
        return [Player(player_id).name, Player(player_id).team_name, 0, 0, 0, 0, 0]

    def create_league_start(self, player_ids):
        league_lst = []

        for player in player_ids:
            league_lst.append(self.create_player_row(player))

        return pd.DataFrame(data = league_lst, columns = self.columns)
    
    def add_result(self):
        pass

    def loop_results(self):
        pass


# print(list(Fixture_Generator(38606).get_fixtures().keys()))
print(League("Hello").create_league_start(list(Fixture_Generator(38606).get_fixtures().keys())))
