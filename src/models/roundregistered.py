from src.models.round import Round


class RoundRegistered(Round):
    def __init__(self, start_time, end_time, name, tournament_name, match=None):
        super().__init__(name, tournament_name, match)
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)
