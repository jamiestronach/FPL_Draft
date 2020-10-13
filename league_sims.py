from fixture_gen import Fixture_Generator
from league import League
from main import league_code
from player import Player


class League_Sims(League):

    def __init__(self, number_simulations):
        self.number_sims = number_simulations
        self.fixture_sets = Fixture_Generator(league_code).get_fixtures_set(number_simulations)
        self.players = [Player(id) for id in self.fixture_sets[0].keys()]
        # Need to sort exceptions for when user enters either 0 or a string / float as the number

    def create_blank_league(self):

        league = self.create_league_start([player.id for player in self.players])       
        league.columns = ["Player_Name", "Team_Name", "AWPS", "ADPS", "ALPS", "APPS", "Average_Position"]
        return league

    def player_WDLP_stats(self, overall_league, league, player_id):
        
        league_conversion = {"Wins": "AWPS", "Draws":"ADPS", "Losses":"ALPS", "Points": "APPS"}

        for column in list(league_conversion.keys()):
            overall_league.at[player_id, league_conversion[column]] = overall_league[league_conversion[column]][player_id] + league[column][player_id]
        
        return overall_league
    
    def player_position_stats(self, overall_league, league, player_id):

        standings = []
        
        for index, row in league.iterrows():
            standings.append(index)

        overall_league.at[player_id, "Average_Position"]  = overall_league["Average_Position"][player_id] + standings.index(player_id) + 1

        return overall_league


    def all_player_WDLP_stats(self, overall_league, league):

        for player in self.fixture_sets[0].keys():
            self.player_WDLP_stats(overall_league, league, player)
            self.player_position_stats(overall_league, league, player)

        return overall_league

    



fixtures = Fixture_Generator(90184).get_fixtures()


leag = League(fixtures).league_table
l = League_Sims(10).create_blank_league()
print(leag)
print(League_Sims(10).all_player_WDLP_stats(l,leag))

# print(leag)

# for index, row in leag.iterrows():
#     print(index)




