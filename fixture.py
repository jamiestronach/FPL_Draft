from fixture_gen import Fixture_Generator

fixtures = Fixture_Generator(38606).get_fixtures()

class Fixture():

    def __init__(self, team, gameweek, fixture_set):

        self.team = team
        self.gameweek = gameweek
        self.opposition = fixture_set[team][gameweek]





print(fixtures)
print(Fixture(150578, 2, fixtures).opposition)