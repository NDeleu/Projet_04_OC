from src.models.mdl_round import Round


class RoundDisplayed(Round):
    def __init__(self, name, tournament_name):
        super().__init__(name, tournament_name)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)
