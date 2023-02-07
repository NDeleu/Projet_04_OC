from src.models.mdl_match import Match


class MatchRegistered(Match):
    def __init__(
            self, player1, player2, result_match,
            name, round_name, tournament_name):
        super().__init__(name, round_name, tournament_name)
        self.player1 = player1
        self.player2 = player2
        if result_match is None:
            self.result_match = ()
        else:
            self.result_match = result_match

    def __str__(self):
        if not self.result_match:
            return f"{self.name} : {self.player1} vs {self.player2}"

        else:
            return f"{self.name} : {self.result_match}"

    def __repr__(self):
        return str(self)
