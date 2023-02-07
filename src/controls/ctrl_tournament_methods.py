import copy

from src.models.mdl_tournament import Tournament
from src.views.view_show_tournament import ShowTournament


class CtrlTournamentMethods:
    def __init__(self, view_main, manager_main, player_methods):
        self.tournament = Tournament
        self.show_tournament = ShowTournament()
        self.view_main = view_main
        self.manager_main = manager_main
        self.player_methods = player_methods
        self.leave_round = LeaveRound()
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
        print(self.show_tournament.init_name_tournament_register(
            self.name_len_min, self.name_len_max))
        answer = self.view_main.view_input.try_string_input(
            self.name_len_min, self.name_len_max)
        if self.view_main.view_input.try_already_exists(
                "nom",
                answer,
                self.manager_main.
                check_main.check_models.check_tournament_exists(answer)):
            return answer
        else:
            return self.name_tournament_register()

    def location_tournament_register(self):
        print(self.show_tournament.init_location_tournament_register(
            self.location_len_min, self.location_len_max))
        return self.view_main.view_input.try_alphanum_string_input(
            self.location_len_min, self.location_len_max)

    def time_control_choice_tournament_register(self):
        print(self.show_tournament.init_time_control_tournament_register())
        answer = self.view_main.view_input.try_choice_input(
            self.time_control_list)
        if answer == "1":
            return self.time_control_string_list[0]
        elif answer == "2":
            return self.time_control_string_list[1]
        elif answer == "3":
            return self.time_control_string_list[2]

    def number_round_tournament_register(self):
        print(
            self.show_tournament.
            init_number_round_choice_tournament_register())
        answer = self.view_main.view_input.try_choice_input(
            self.number_round_choice)
        if answer == "1":
            return self.default_number_round
        elif answer == "2":
            print(self.show_tournament.
                  init_number_round_wanted_tournament_register())
            return self.view_main.view_input.try_is_not_digit()

    def description_tournament_register(self):
        print(
            self.show_tournament.init_description_choice_tournament_register())
        answer = self.view_main.view_input.try_choice_input(
            self.description_choice)
        if answer == "1":
            print(
                self.show_tournament.
                init_description_string_tournament_register(
                    self.description_len_min, self.description_len_max))
            return self.view_main.view_input.try_string_input(
                self.description_len_min, self.description_len_max)
        elif answer == "2":
            return self.default_description

    def init_create_tournament_registered(self):
        dict_to_record = self.init_dict_tournament_register()
        return self.tournament(**dict_to_record)

    def register_tournament(self):
        tournament_instance = self.init_create_tournament_registered()
        self.manager_main.manager_insert.insert_tournament_to_database(
            tournament_instance.__dict__)
        if self.manager_main.check_main.check_models.check_tournament_exists(
                tournament_instance.name):
            print(
                self.show_tournament.validate_creation_tournament(
                    tournament_instance))
        else:
            print(self.view_main.view_input.show_error_input.error_record())
            return self.register_tournament()

    def load_tournament(self):
        print(self.show_tournament.init_load_tournament(
            self.name_len_min, self.name_len_max))
        answer = self.view_main.view_input.try_string_input(
            self.name_len_min, self.name_len_max)
        if self.view_main.view_input.try_not_exists(
                "nom",
                answer,
                self.manager_main.check_main.check_models.
                check_tournament_exists(answer)):
            return answer
        else:
            return None

    def load_id_player_to_tournament(self):
        print(self.show_tournament.show_load_id_player_to_tournament())
        answer = self.view_main.view_input.try_id_player_input()
        if self.view_main.view_input.try_not_exists(
                "identifiant joueur",
                answer,
                self.manager_main.check_main.check_models.
                check_player_exists(answer)):
            return answer
        else:
            return False

    def create_id_player_to_tournament(self):
        answer = self.player_methods.register_player_for_tournament()
        if answer is False:
            return False
        else:
            return answer

    def choice_id_player_to_tournament(self, player_list):
        print(self.show_tournament.show_choice_id_player_to_tournament())
        answer = self.view_main.view_input.try_choice_input([1, 2])
        if answer == "1":
            answer_1_a = self.load_id_player_to_tournament()
            if answer_1_a is False:
                return self.choice_id_player_to_tournament(player_list)
            else:
                answer_1_b = self.check_player_in_player_list_tournament(
                    player_list, answer_1_a)
                if answer_1_b is False:
                    return self.choice_id_player_to_tournament(player_list)
                else:
                    return answer_1_b
        elif answer == "2":
            answer_2_a = self.create_id_player_to_tournament()
            if answer_2_a is False:
                return self.choice_id_player_to_tournament(player_list)
            else:
                return answer_2_a

    def check_player_in_player_list_tournament(
            self, player_list, tested_id_player):
        if not player_list:
            return tested_id_player
        else:
            for player in player_list:
                if player.id_chess == tested_id_player:
                    print(
                        self.show_tournament.
                        show_error_check_player_in_player_list_tournament())
                    return False
            return tested_id_player

    def save_list_player_to_database(self, tournament_name, list_player):
        self.manager_main.manager_insert.\
            insert_players_to_tournament_to_database(
                tournament_name,
                self.manager_main.manager_format.
                format_update_players_to_tournament_to_database(list_player))

    def replace_player_list_dict_to_instance(self, list_player):
        new_list = []
        for player_dict in list_player:
            new_list.append(
                self.player_methods.id_player_to_inst_player_displayed(
                    player_dict["id_chess"]))
        return new_list

    def completed_player_in_list_player(self, list_player):
        print(self.show_tournament.show_completed_player_in_list_player())
        self.show_tournament.show_all_player_in_list_player(list_player)
        print("\n")

    def not_enough_player_in_list_player(self, list_player):
        print(self.show_tournament.show_not_enough_player_in_list_player(
            list_player))
        self.show_tournament.show_all_player_in_list_player(list_player)
        print("\n")

    def no_player_in_list_player(self):
        print(self.show_tournament.show_no_player_in_list_player())
        print("\n")

    def success_add_player(self):
        print(self.show_tournament.show_success_add_player())

    def save_list_date_to_database(self, tournament_name, list_date):
        self.manager_main.manager_insert.insert_date_to_tournament_to_database(
            tournament_name, list_date)

    def update_date_start_round(self, name, tournament_name, list_date):
        answer = self.manager_main.check_main.check_models.\
            return_date_start_round(name, tournament_name)
        if answer not in list_date:
            return answer
        else:
            return None

    def update_date_end_round(self, name, tournament_name, list_date):
        answer = self.manager_main.check_main.check_models.\
            return_date_end_round(name, tournament_name)
        if answer not in list_date:
            return answer
        else:
            return None

    def leave_rounds(self, method_tried):
        if method_tried is False:
            raise self.leave_round
        return method_tried

    def end_tournament(self, tournament_inst):
        print(self.show_tournament.show_end_tournament(
            tournament_inst.name,
            tournament_inst.date[len(tournament_inst.date) - 1]))
        print(self.show_tournament.show_init_result_end_tournament())
        list_player = copy.deepcopy(tournament_inst.player_list)
        list_player_by_round_point = copy.deepcopy(
            self.player_methods.init_player_round_point_calculated(
                tournament_inst.name, list_player))
        list_player_order_round_point = sorted(
            list_player_by_round_point,
            key=lambda x: x.round_point, reverse=True)
        for player in list_player_order_round_point:
            print(self.show_tournament.show_result_end_tournament(
                player.name,
                player.surname,
                player.id_chess,
                player.round_point))

    def tournament_keep_running(): # à modifier plus tard
        answer = input("1 pour quitter, 2 pour continuer")
        if answer == "1":
            return False
        elif answer == "2":
            return True

    tournament_keep_running = staticmethod(tournament_keep_running)


class LeaveRound(Exception):
    pass
