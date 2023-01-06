from src.models import Player


class ControlPlayer:
    def __init__(self, manager):
        self.player = Player
        self.manager = manager

    def init_player(self, name, surname, naissance, identifiant):
        return self.player(name, surname, naissance, identifiant)

    def add_player(self, name, surname, naissance, identifiant):
        self.manager.list_all_player.append(self.init_player(name, surname, naissance, identifiant))
        self.manager.creat_player_to_json(len(self.manager.list_all_player))

    def load_player(self, player_number):
        self.manager.list_all_player.append(
            self.player(**self.manager.load_player_to_json(player_number)))

    def calcul_total_point(self, players):
        for tournoi in self.manager.list_all_tournoi:
            for rounding in tournoi.round:
                for matching in rounding.match:
                    if players == matching.result_match[0][0]:
                        players.total_point += matching.result_match[0][1]
                    elif players == matching.result_match[1][0]:
                        players.total_point += matching.result_match[1][1]

    def init_total_point(self):
        for players in self.manager.list_all_player:
            players.total_point = 0
            self.calcul_total_point(players)
