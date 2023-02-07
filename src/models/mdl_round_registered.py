from src.models.mdl_round import Round


class RoundRegistered(Round):
    def __init__(
            self, start_time, name,
            tournament_name, end_time=None, match=None):
        super().__init__(name, tournament_name, match)
        self.start_time = start_time
        if end_time is None:
            self.end_time = "Le Round n'est pas encore terminé"
        else:
            self.end_time = end_time

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)
