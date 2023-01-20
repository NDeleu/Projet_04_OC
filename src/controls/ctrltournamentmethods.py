from src.models.tournament import Tournament
from src.views.showtournament import ShowTournament


class CtrlTournamentMethods:
    def __init__(self, view_main, manager_main):
        self.tournament = Tournament
        self.show_tournament = ShowTournament()
        self.view_main = view_main
        self.manager_main = manager_main
        self.name_len_min = 3
        self.name_len_max = 20
        self.location_len_min = 2
        self.location_len_max = 12
        self.time_control_list = [1, 2, 3]
        self.time_control_string_list = ["Blitz", "Coup Rapide", "Bullet"]
        self.number_round_choice = [1, 2]
        self.default_number_round = "4"
        self.description_choice = [1, 2]
        self.default_description = "Aucune description"
        self.description_len_min = 1
        self.description_len_max = 42

    def init_dict_tournament_register(self):
        return {"name": self.name_tournament_register(),
                "location": self.location_tournament_register(),
                "time_control": self.time_control_choice_tournament_register(),
                "number_round": self.number_round_tournament_register(),
                "description": self.description_tournament_register()}

    def name_tournament_register(self):
        print(self.show_tournament.init_name_tournament_register(self.name_len_min, self.name_len_max))
        answer = self.view_main.view_input.try_string_input(self.name_len_min, self.name_len_max)
        if self.view_main.view_input.try_already_exists(
                "nom", answer, self.manager_main.check_main.check_models.check_tournament_exists(answer)):
            return answer
        else:
            return self.name_tournament_register()

    def location_tournament_register(self):
        print(self.show_tournament.init_location_tournament_register(self.location_len_min, self.location_len_max))
        return self.view_main.view_input.try_alphanum_string_input(self.location_len_min, self.location_len_max)

    def time_control_choice_tournament_register(self):
        print(self.show_tournament.init_time_control_tournament_register())
        answer = self.view_main.view_input.try_choice_input(self.time_control_list)
        if answer == "1":
            return self.time_control_string_list[0]
        elif answer == "2":
            return self.time_control_string_list[1]
        elif answer == "3":
            return self.time_control_string_list[2]

    def number_round_tournament_register(self):
        print(self.show_tournament.init_number_round_choice_tournament_register())
        answer = self.view_main.view_input.try_choice_input(self.number_round_choice)
        if answer == "1":
            return self.default_number_round
        elif answer == "2":
            print(self.show_tournament.init_number_round_wanted_tournament_register())
            return self.view_main.view_input.try_is_not_digit()

    def description_tournament_register(self):
        print(self.show_tournament.init_description_choice_tournament_register())
        answer = self.view_main.view_input.try_choice_input(self.description_choice)
        if answer == "1":
            print(self.show_tournament.init_description_string_tournament_register(
                self.description_len_min, self.description_len_max))
            return self.view_main.view_input.try_string_input(
                self.description_len_min, self.description_len_max)
        elif answer == "2":
            return self.default_description


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