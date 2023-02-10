
from src.models import Player


class PlayerDisplayed(Player):
    def __init__(self, name, surname, id_chess):
        super().__init__(name, surname, id_chess)
        self.round_point = 0
        self.encountered = []

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return str(self)
