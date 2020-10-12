from pull_data import Pull_Data
from main import league_data

league_code = 38606

class Player():

    def __init__(self, id):

        self.id = id
        self.score = league_data.scores[self.id]        
        self.name = league_data.player_names[self.id]
        self.team_name = league_data.team_names[self.id]
        self.best_finish = ""
        self.worst_finish = ""
        self.average_finish = ""
        self.mode_finish = ""

