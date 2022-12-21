

class Match:
    def __init__(self, player1, player2):
        self.name = str
        self.player1 = player1
        self.player2 = player2
        self.result_player1 = int
        self.result_player2 = int
        self.result_match = ()

    def __str__(self):
        if not self.result_match:
            return f"{self.name} : {self.player1} vs {self.player2} : résultat à définir"

        else:
            return f"{self.name} : {self.result_match}"

    def __repr__(self):
        return str(self)

