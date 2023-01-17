from src.models import Match


class MatchDisplayed(Match):
    def __init__(self, name, round_name, tournament_name):
        super().__init__(name, round_name, tournament_name)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)

