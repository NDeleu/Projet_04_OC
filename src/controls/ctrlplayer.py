from src.models import Player


class ControlPlayer:
    def __init__(self, manager):
        self.player = Player
        self.manager = manager

    def init_player(self, name, surname, age, rank):
        return self.player(name, surname, age, rank)

    def add_player(self, name, surname, age, rank):
        self.manager.list_all_player.append(self.init_player(name, surname, age, rank))
