from src.models import Tournoi


class ControlTournoi:
    def __init__(self, manager, round_control):
        self.tournoi = Tournoi
        self.manager = manager
        self.round_control = round_control

    def init_tournoi(self, name, lieu, control_temps, tours_round=4):
        return self.tournoi(name, lieu, control_temps, tours_round)

    def add_tournoi(self, name, lieu, control_temps, tours_round=4):
        self.manager.list_all_tournoi.append(self.init_tournoi(
            name, lieu, control_temps, tours_round))

    def add_player_tournoi(self, tournoi_number, player):
        self.manager.list_all_tournoi[tournoi_number-1].player_list.append(player)

    def start_tournoi(self, tournoi_number):
        if not self.manager.list_all_tournoi[tournoi_number-1].round:
            self.round_control.add_round(tournoi_number, 1)
        else:
            """
            if len(self.manager.list_all_tournoi[
                       tournoi_number-1].round) == self.manager.list_all_tournoi[
                tournoi_number-1].tours_round and self.manager.list_all_tournoi[tournoi_number-1].round[len(
                        self.manager.list_all_tournoi[tournoi_number-1].round)-1].end_time:
                print("Fin du tournoi. /n Classement des joueurs par points : ", sorted(
                    self.manager.list_all_tournoi[tournoi_number-1].player_list, key=lambda x: x.round_point))
            else:
            """
            if self.manager.list_all_tournoi[tournoi_number-1].round[len(
                    self.manager.list_all_tournoi[tournoi_number-1].round)-1].end_time:
                self.round_control.add_round(tournoi_number, len(
                    self.manager.list_all_tournoi[tournoi_number-1].round)+1)
            else:
                self.round_control.test_round(tournoi_number, len(
                    self.manager.list_all_tournoi[tournoi_number-1].round))
