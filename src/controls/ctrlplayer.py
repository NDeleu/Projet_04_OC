from src.models import Player


class ControlPlayer:
    def __init__(self, manager):
        self.player = Player
        self.manager = manager

    def init_player(self, name, surname, naissance, identifiant, rank):
        return self.player(name, surname, naissance, identifiant, rank)

    def add_player(self, name, surname, naissance, identifiant, rank):
        self.manager.list_all_player.append(self.init_player(name, surname, naissance, identifiant, rank))
