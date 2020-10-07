from pull_data import Pull_Data

league_code = 38606

class Player():

    data = Pull_Data(league_code)

    def __init__(self, id):

        self.id = id
        self.score = self.data.get_scores()[self.id]        
        self.name = self.data.get_player_names()[self.id]
        self.team_name = self.data.get_team_names()[self.id]
        self.best_finish = ""
        self.worst_finish = ""
        self.average_finish = ""
        self.mode_finish = ""


    

print(Player(150578).team_name)
print(Player(150578).name)
print(Player(150578).score)