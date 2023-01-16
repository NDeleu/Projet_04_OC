from src.models import Tournament
from src.views import ShowTournament


class CtrlTournamentMethods:
    def __init__(self):
        self.tournament = Tournament
        self.show_tournament = ShowTournament


"""
class ControlTournoi:
    def __init__(self, manager, round_control, player_control):
        self.tournoi = Tournoi
        self.manager = manager
        self.round_control = round_control
        self.player_control = player_control

    def init_tournoi(self, name, lieu, control_temps, tours_round=4):
        return self.tournoi(name, lieu, control_temps, tours_round)

    def add_tournoi(self, name, lieu, control_temps, tours_round=4):
        self.manager.list_all_tournoi.append(self.init_tournoi(
            name, lieu, control_temps, tours_round))
        self.manager.creat_tournoi_to_json(len(self.manager.list_all_tournoi))

    def load_tournoi_by_name(self, name):
        self.manager.list_all_tournoi.append(self.tournoi(**self.manager.load_tournoi_to_json_by_name(name)))
        for i in range(len(self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round)):
            self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round[i] = self.round_control.round(
                **self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round[i])
            self.round_control.load_round_by_name(i)
            self.link_player_tournoi()

    def load_tournoi_by_id(self, id_tournoi):
        self.manager.list_all_tournoi.append(self.tournoi(**self.manager.load_tournoi_to_json_by_id(id_tournoi)))
        self.link_player_tournoi()
        for i in range(len(self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round)):
            self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round[i] = self.round_control.round(
                **self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round[i])
            self.round_control.load_round_by_id(i)

    def link_player_tournoi(self):
        for plyer in self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].player_list:
            if not self.manager.link_player_class(plyer):
                pass
            else:
                self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].player_list[
                    self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].player_list.index(plyer)] = \
                    self.manager.link_player_class(plyer)

    def load_all_tournoi(self):
        for y in range(self.manager.len_list_tournoi()):
            self.load_tournoi_by_id(y+1)

    def creat_add_player_tournoi(self, tournoi_number, name, surname, naissance, identifiant):
        self.player_control.add_player(name, surname, naissance, identifiant)
        self.add_player_tournoi(tournoi_number, self.manager.list_all_player[len(self.manager.list_all_player)-1])

    def load_add_player_tournoi(self, tournoi_number, identifiant_player):
        self.player_control.load_player_by_idplayer(identifiant_player)
        self.add_player_tournoi(tournoi_number, self.manager.list_all_player[len(self.manager.list_all_player)-1])

    def add_player_tournoi(self, tournoi_number, player):
        self.manager.list_all_tournoi[tournoi_number-1].player_list.append(player)

    def start_tournoi(self, tournoi_number):
        if not self.manager.list_all_tournoi[tournoi_number-1].round:
            self.round_control.add_round(tournoi_number, 1)
        else:
            if len(self.manager.list_all_tournoi[
                       tournoi_number-1].round) == self.manager.list_all_tournoi[
                tournoi_number-1].tours_round and self.manager.list_all_tournoi[tournoi_number-1].round[len(
                        self.manager.list_all_tournoi[tournoi_number-1].round)-1].end_time:
                print("Fin du tournoi le ", self.manager.list_all_tournoi[tournoi_number-1].round[len(
                        self.manager.list_all_tournoi[tournoi_number-1].round)-1].end_time)
                print("Classement des joueurs par points : ")
                self.round_control.init_round_point(tournoi_number)
                for player in sorted(self.manager.list_all_tournoi[tournoi_number-1].player_list,
                                     key=lambda x: x.round_point, reverse=True):
                    print(player, " ", player.round_point, "points")
                self.manager.save_date_tournoi_to_json(tournoi_number)
                self.manager.save_round_tournoi_to_json(tournoi_number)
                self.manager.clear_list_tournoi()
                self.manager.clear_list_player()
                self.player_control.load_all_player()
                self.load_all_tournoi()
                self.player_control.init_total_point()
                self.manager.clear_list_player()
                self.manager.clear_list_tournoi()
            else:
                if self.manager.list_all_tournoi[tournoi_number-1].round[len(
                        self.manager.list_all_tournoi[tournoi_number-1].round)-1].end_time:
                    self.manager.save_date_tournoi_to_json(tournoi_number)
                    self.manager.save_round_tournoi_to_json(tournoi_number)
                    self.round_control.add_round(tournoi_number, len(
                        self.manager.list_all_tournoi[tournoi_number-1].round)+1)
                else:
                    self.round_control.test_round(tournoi_number, len(
                        self.manager.list_all_tournoi[tournoi_number-1].round))
"""