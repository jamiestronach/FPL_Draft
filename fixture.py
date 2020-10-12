from fixture_gen import Fixture_Generator
from main import league_data


class Fixture():

    def __init__(self, team, gameweek, fixture_set):

        self.team = team
        self.gameweek = gameweek
        self.opposition = fixture_set[team][gameweek]
        self.team_score = league_data.scores[self.team][self.gameweek]
        self.opposition_score = league_data.scores[self.opposition][self.gameweek]
        self.outcome_points = self.match_outcome()

    def match_outcome(self):

        if self.team_score > self.opposition_score:
            return 3
        elif self.team_score == self.opposition_score:
            return 1
        else:
            return 0
