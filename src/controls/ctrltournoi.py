from src.models import Tournoi


class ControlTournoi:
    def __init__(self, manager):
        self.tournoi = Tournoi
        self.manager = manager

    def init_tournoi(self, name, lieu, player_list, control_temps, tours_round=4):
        return self.tournoi(name, lieu, player_list, control_temps, tours_round)

    def add_tournoi(self, name, lieu, player_list, control_temps, tours_round=4):
        self.manager.list_all_tournoi.append(self.init_tournoi(
            name, lieu, player_list, control_temps, tours_round))
