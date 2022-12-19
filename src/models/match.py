

class Match:
    def __init__(self, matching_players):
        self.name = str
        self.matching_players = matching_players
        self.result = ([], [])

    def __str__(self):
        if not self.result[0] or not self.result[1]:
            return f"{self.name} : {self.matching_players[0]} contre {self.matching_players[1]} : résultat à définir"
        else:
            return f"{self.name} : {self.result[0][0]} : {self.result[0][1]}, {self.result[1][0]} : {self.result[1][1]}"

    def __repr__(self):
        return str(self)


