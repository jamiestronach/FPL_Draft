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
        league["Avg_Position"] = 0
        return league


    
print(League_Sims(10).create_blank_league())




