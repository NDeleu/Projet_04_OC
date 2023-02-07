import copy

from src.models.mdl_player_displayed import PlayerDisplayed
from src.models.mdl_player_registered import PlayerRegistered
from src.views.view_show_player import ShowPlayer


class CtrlPlayerMethods:
    def __init__(self, view_main, manager_main):
        self.player_registered = PlayerRegistered
        self.player_displayed = PlayerDisplayed
        self.show_player = ShowPlayer()
        self.view_main = view_main
        self.manager_main = manager_main
        self.name_len_min = 3
        self.name_len_max = 15
        self.surname_len_min = 3
        self.surname_len_max = 15

    def init_dict_player_register(self):
        return {"name": self.name_player_register(),
                "surname": self.surname_player_register(),
                "id_chess": self.id_chess_player_register(),
                "total_points": 0,
                "birthday": self.birthday_player_register()}

    def name_player_register(self):
        print(self.show_player.init_name_player_register(
            self.name_len_min, self.name_len_max))
        return self.view_main.view_input.try_alphanum_string_input(
            self.name_len_min, self.name_len_max)

    def surname_player_register(self):
        print(self.show_player.init_surname_player_register(
            self.surname_len_min, self.surname_len_max))
        return self.view_main.view_input.try_alphanum_string_input(
            self.surname_len_min, self.surname_len_max)

    def id_chess_player_register(self):
        print(self.show_player.init_id_chess_player_register())
        answer = self.view_main.view_input.try_id_player_input()
        if self.view_main.view_input.try_already_exists(
                "identifiant joueur",
                answer,
                self.manager_main.check_main.check_models.check_player_exists(
                    answer)):
            return answer
        else:
            return self.id_chess_player_register()

    def birthday_player_register(self):
        print(self.show_player.init_birthday_player_register())
        answer = self.view_main.view_input.try_date_input()
        return answer.strftime("%Y-%m-%d")

    def init_create_player_registered(self):
        dict_to_record = self.init_dict_player_register()
        return self.player_registered(**dict_to_record)

    def open_player_displayed(self, dict_to_record):
        return self.player_displayed(**dict_to_record)

    def list_player_displayed(self, list_dict):
        list_player_disp = []
        for player in list_dict:
            list_player_disp.append(
                self.open_player_displayed(
                    self.manager_main.manager_format.
                    player_register_to_displayed(player)))
        return list_player_disp

    def list_all_player_displayed(self):
        return self.list_player_displayed(
            self.manager_main.check_main.
            check_models.open_list_all_player_dict())

    def register_player(self):
        player_instance = self.init_create_player_registered()
        self.manager_main.manager_insert.insert_player_to_database(
            player_instance.__dict__)
        if self.manager_main.check_main.check_models.check_player_exists(
                player_instance.id_chess):
            print(self.show_player.validate_creation_player(player_instance))
        else:
            print(self.view_main.view_input.show_error_input.error_record())
            return self.register_player()

    def register_player_for_tournament(self):
        player_instance = self.init_create_player_registered()
        self.manager_main.manager_insert.insert_player_to_database(
            player_instance.__dict__)
        if self.manager_main.check_main.check_models.check_player_exists(
                player_instance.id_chess):
            print(self.show_player.validate_creation_player(player_instance))
            return player_instance.id_chess
        else:
            print(self.view_main.view_input.show_error_input.error_record())
            return False

    def id_player_to_inst_player_displayed(self, id_player):
        return self.player_displayed(
            **self.manager_main.manager_format.player_register_to_displayed(
                self.manager_main.check_main.check_models.open_load_player(
                    id_player)))

    def init_player_round_point_calculated(self, tournament_name, list_player):
        new_list_player = copy.deepcopy(list_player)
        for player in new_list_player:
            player.round_point = self.manager_main.check_main.check_results.\
                check_round_point_player(tournament_name, player.id_chess)
        return new_list_player

    def init_player_encountered_updated(self, tournament_name, list_player):
        new_list_player = copy.deepcopy(list_player)
        for player in new_list_player:
            player.encountered = self.manager_main.check_main.check_results.\
                check_encountered_player(tournament_name, player.id_chess)
        return new_list_player

    def init_player_round_point_encountered(
            self, tournament_name, list_player):
        new_list_player = copy.deepcopy(list_player)
        list_with_round_point = self.init_player_round_point_calculated(
            tournament_name, new_list_player)
        list_with_round_point_encountered = \
            self.init_player_encountered_updated(
                tournament_name, list_with_round_point)
        return list_with_round_point_encountered

    def player_total_point_calculated(self, list_player):
        list_player_registered = []
        for player_to_registered in list_player:
            list_player_registered.append(
                self.player_registered(
                    **self.manager_main.check_main.check_models.
                    open_load_player(player_to_registered.id_chess)))
        for player in list_player_registered:
            player.total_points = self.manager_main.check_main.check_results.\
                check_total_point_player(player.id_chess)
            self.manager_main.manager_insert.\
                insert_total_points_to_player_to_database(
                    player.total_points, player.id_chess)
