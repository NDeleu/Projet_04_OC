from src.models import Player


class ControlPlayer:
    def __init__(self, manager):
        self.player = Player
        self.manager = manager

    def init_player(self, name, surname, naissance, identifiant):
        return self.player(name, surname, naissance, identifiant)

    def add_player(self, name, surname, naissance, identifiant):
        self.manager.list_all_player.append(self.init_player(name, surname, naissance, identifiant))
