from main import league_data

class Player():

    def __init__(self, id):

        self.id = id
        self.score = league_data.scores[self.id]        
        self.name = league_data.player_names[self.id]
        self.team_name = league_data.team_names[self.id]
        self.best_finish = 0
        self.best_finish_fixture = ""
        self.worst_finish = 0
        self.worst_finish_fix = ""
        self.average_finish = 0
        self.mode_finish = 0

