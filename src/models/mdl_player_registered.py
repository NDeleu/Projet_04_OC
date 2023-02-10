
from src.models import Player


class PlayerRegistered(Player):
    def __init__(self, birthday, total_points, name, surname, id_chess):
        super().__init__(name, surname, id_chess)
        self.birthday = birthday
        self.total_points = total_points

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return str(self)
