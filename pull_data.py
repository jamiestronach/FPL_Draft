import requests
import json

class Pull_Data():

    payload = {}
    headers = {
        'authority': 'draft.premierleague.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://draft.premierleague.com/league',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_fbp=fb.1.1591974378630.1388117418; csrftoken=o0HBg1soXqEfafytSpwUfJn4zlPLE375mzYTzfkasL73943bKWlUpTniP9JXOIHi; _gid=GA1.2.543120220.1601327503; pl_profile=eyJzIjogIld6SXNORGMwT1RJME5sMDoxa04wUkU6Qkl5V0xfZE1ScmZUa202MWdCNFlNVE13SEIwIiwgInUiOiB7ImlkIjogNDc0OTI0NiwgImZuIjogIkphbWllIiwgImxuIjogIlN0cm9uYWNoIiwgImZjIjogbnVsbH19; sessionid=i3kql0dtznsk8uu4nf2ree1qy0lbo8z9; activeEntry=150310; _ga_NREXP8D25C=GS1.1.1601551710.68.0.1601551710.0; _ga=GA1.2.864881373.1589897324'
        }

    def __init__(self, league_code):
        self.league_code = str(league_code)
        self.url = "https://draft.premierleague.com/api/league/" + self.league_code + "/details"
        
    def get_response(self):
        response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
        return response

    def get_json(self):
        json_object = self.get_response().json()
        return json_object

    def get_number_players(self):
        return len(self.get_json()["league_entries"])

    def get_player_names(self):
        names = {}
        
        for player in self.get_json()["league_entries"]:
            names[player["id"]] = {"name" : f"{player['player_first_name']} {player['player_last_name']}"}
        
        return names

    def _get_player_scores(self):
        names = self.get_player_names()

        for game in self.get_json()["matches"]:
            for player in ["1", "2"]:
                if game[f"league_entry_{player}"] in names:
                    names[game[f"league_entry_{player}"]][f'''GW{game["event"]}'''] = game[f"league_entry_{player}_points"]
            
        return names

    def get_last_active_gameweek(self):
        names = self._get_player_scores()

        for week in range(1,39):
            GW = week
            inactive_players = 0 
            for player in names.keys():
                if names[player][f'''GW{week}'''] == 0:
                    inactive_players += 1
                    if inactive_players >= 2: 
                        return GW -1

    def _remove_blank_weeks(self):
        last_GW = self.get_last_active_gameweek()
        names = self._get_player_scores()

        for week in range(last_GW + 1, 39):
            for player in names.keys():
                del names[player][f'''GW{week}''']

        return names

    def get_scores(self):
        return self._remove_blank_weeks()

                        


print(Pull_Data(38606).get_scores())