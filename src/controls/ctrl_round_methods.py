import copy
import random

from src.models.mdl_round_displayed import RoundDisplayed
from src.models.mdl_round_registered import RoundRegistered
from src.views.view_show_round import ShowRound
import datetime


class CtrlRoundMethods:
    def __init__(self, manager_main, player_methods, view_main):
        self.round_registered = RoundRegistered
        self.round_displayed = RoundDisplayed
        self.show_round = ShowRound()
        self.manager_main = manager_main
        self.player_methods = player_methods
        self.view_main = view_main

    def init_dict_round_register(name, tournament_name):
        return {"name": name,
                "tournament_name": tournament_name,
                "start_time": datetime.datetime.now().strftime("%Y-%m-%d")}

    init_dict_round_register = staticmethod(init_dict_round_register)

    def init_create_round_registered(self, name, tournament_name):
        dict_to_record = self.init_dict_round_register(name, tournament_name)
        return self.round_registered(**dict_to_record)

    def register_round(self, name, tournament_name):
        round_instance = self.init_create_round_registered(
            name, tournament_name)
        self.manager_main.manager_insert.insert_rounds_to_database(
            round_instance.__dict__)

    def load_round_to_tournament(self, name, tournament_name):
        return self.round_displayed(
            **self.manager_main.manager_format.
            round_register_to_displayed(
                self.manager_main.check_main.check_models.open_load_rounds(
                    name, tournament_name)))

    def replace_rounds_list_dict_to_instance(
            self, list_round, tournament_name):
        new_list = []
        for rounds_dict in list_round:
            new_list.append(
                self.load_round_to_tournament(rounds_dict["name"],
                                              tournament_name))
        return new_list

    def register_and_load_round_to_tournament(self, name, tournament_name):
        self.register_round(name, tournament_name)
        return self.load_round_to_tournament(name, tournament_name)

    def save_list_round_to_database(self, tournament_name, list_rounds):
        self.manager_main.manager_insert.\
            insert_rounds_to_tournament_to_database(
                tournament_name,
                self.manager_main.manager_format.
                format_update_rounds_to_tournament_to_database(list_rounds))

    def init_first_round(self, player_list):
        list_id_and_couple_player = []
        list_player = copy.deepcopy(player_list)
        random.shuffle(list_player)
        for y in range(int(len(list_player) / 2)):
            list_id_and_couple_player.append(
                (y + 1, self.couple_player_match(
                    list_player[y],
                    list_player[y + (int(len(list_player) / 2))])))
        return list_id_and_couple_player

    def init_other_round(self, tournament_name, player_list):
        list_id_and_couple_player = []
        list_player = copy.deepcopy(
            self.player_methods.init_player_round_point_encountered(
                tournament_name, player_list))
        list_player_by_round_point = sorted(
            list_player, key=lambda x: x.round_point, reverse=True)
        list_player_by_round_point_extend = copy.deepcopy(
            list_player_by_round_point)
        list_player_by_round_point_extend.append("Out")
        for y in range(int(len(list_player_by_round_point) / 2)):
            list_id_and_couple_player.append(
                (y + 1,
                 self.couple_player_match(
                     self.test_player1_in_list_couple(
                         list_player_by_round_point_extend,
                         list_id_and_couple_player),
                     self.test_player2_in_list_couple(
                         list_player_by_round_point_extend,
                         list_id_and_couple_player))))
        return list_id_and_couple_player

    def test_player1_in_list_couple(self, list_player, list_couple):
        if list_couple:
            for player in list_player:
                if self.test_is_in_couple(list_couple, player):
                    pass
                else:
                    return player
        else:
            return list_player[0]

    def test_player2_in_list_couple(self, list_player, list_couple):
        if list_couple:
            for player in list_player:
                if player == "Out":
                    for players in list_player:
                        if self.test_is_in_couple(list_couple, players):
                            pass
                        elif players == self.test_player1_in_list_couple(
                                list_player, list_couple):
                            pass
                        else:
                            return players
                else:
                    if self.test_is_in_couple(list_couple, player):
                        pass
                    elif player == self.test_player1_in_list_couple(
                            list_player, list_couple):
                        pass
                    elif self.test_is_encountered(
                            self.test_player1_in_list_couple(
                                list_player, list_couple).encountered,
                            player.id_chess):
                        pass
                    else:
                        return player
        else:
            for player in list_player:
                if player == "Out":
                    for players in list_player:
                        if players == list_player[0]:
                            pass
                        else:
                            return players
                else:
                    if player == list_player[0]:
                        pass
                    elif self.test_is_encountered(
                            self.test_player1_in_list_couple(
                                list_player, list_couple).encountered,
                            player.id_chess):
                        pass
                    else:
                        return player

    def test_is_in_couple(list_couple, player):
        for couple in list_couple:
            if couple[1][0] == player or couple[1][1] == player:
                return True

    test_is_in_couple = staticmethod(test_is_in_couple)

    def test_is_encountered(list_encountered, id_player_tested):
        for id_counter in list_encountered:
            if id_counter == id_player_tested:
                return True

    test_is_encountered = staticmethod(test_is_encountered)

    def couple_player_match(player1, player2):
        return player1, player2

    couple_player_match = staticmethod(couple_player_match)

    def check_all_match_played(list_match):
        for match in list_match:
            if not match.result_match:
                return False
            else:
                pass
        return True

    check_all_match_played = staticmethod(check_all_match_played)

    def show_end_round(self, round_name):
        print(self.show_round.init_show_end_round(round_name))
        print(self.show_round.init_show_result_match())

    def add_end_time_round(self, tournament_name, round_name):
        self.manager_main.manager_insert.insert_end_time_to_rounds_to_database(
            tournament_name,
            round_name,
            datetime.datetime.now().strftime("%Y-%m-%d"))

    def show_create_round(self, round_name):
        print(self.show_round.init_show_create_round(round_name))

    def resume_round(self, round_name):
        print(self.show_round.init_resume_round(round_name))
