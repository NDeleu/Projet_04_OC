from src.models.mdl_match_registered import MatchRegistered
from src.models.mdl_match_displayed import MatchDisplayed
from src.views.view_show_match import ShowMatch


class CtrlMatchMethods:
    def __init__(self, manager_main, player_methods, view_main):
        self.match_registered = MatchRegistered
        self.match_displayed = MatchDisplayed
        self.show_match = ShowMatch()
        self.manager_main = manager_main
        self.player_methods = player_methods
        self.view_main = view_main
        self.enter_result_match_choice = [1, 2, 3]

    def init_dict_create_match(self, name, round_name, tournament_name, player1, player2):
        return {"name": name,
                "round_name": round_name,
                "tournament_name": tournament_name,
                "player1": self.manager_main.manager_format.player_register_to_displayed(player1.__dict__),
                "player2": self.manager_main.manager_format.player_register_to_displayed(player2.__dict__),
                "result_match": None}

    def init_create_match_registered(self, name, round_name, tournament_name, player1, player2):
        dict_to_record = self.init_dict_create_match(name, round_name, tournament_name, player1, player2)
        return self.match_registered(**dict_to_record)

    def register_match(self, name, round_name, tournament_name, player1, player2):
        match_instance = self.init_create_match_registered(name, round_name, tournament_name, player1, player2)
        self.manager_main.manager_insert.insert_matches_to_database(match_instance.__dict__)

    def load_match_to_round(self, name, round_name, tournament_name):
        return self.match_displayed(**
                                    self.manager_main.manager_format.match_register_to_displayed(
                                        self.manager_main.check_main.check_models.open_load_matches(
                                            name, round_name, tournament_name)))

    def register_and_load_match_to_round(self, name, round_name, tournament_name, player1, player2):
        self.register_match(name, round_name, tournament_name, player1, player2)
        return self.load_match_to_round(name, round_name, tournament_name)

    def replace_match_list_dict_to_instance(self, list_match):
        new_list = []
        for match_dict in list_match:
            new_list.append(self.dict_match_to_inst_match_with_player(
                match_dict["name"], match_dict["round_name"], match_dict["tournament_name"]))
        return new_list

    def dict_match_to_inst_match_without_player(self, name, round_name, tournament_name):
        return self.match_registered(**
                                     self.manager_main.check_main.check_models.open_load_matches(
                                         name, round_name, tournament_name))

    def dict_match_to_inst_match_with_player(self, name, round_name, tournament_name):
        instance = self.dict_match_to_inst_match_without_player(name, round_name, tournament_name)
        instance.player1 = self.player_methods.id_player_to_inst_player_displayed(instance.player1["id_chess"])
        instance.player2 = self.player_methods.id_player_to_inst_player_displayed(instance.player2["id_chess"])
        return instance

    def save_list_match_to_database(self, tournament_name, round_name, list_matches):
        self.manager_main.manager_insert.insert_matches_to_rounds_to_database(
            tournament_name,
            round_name,
            self.manager_main.manager_format.format_update_rounds_to_tournament_to_database(list_matches))

    def enter_result_match(self, player1, player2):
        print(self.show_match.show_init_enter_result_match())
        print(self.show_match.show_enter_result_match(player1, player2))
        answer = self.view_main.view_input.try_choice_input(self.enter_result_match_choice)
        if answer == "1":
            return [(self.manager_main.manager_format.player_register_to_displayed(player1.__dict__), 1),
                    (self.manager_main.manager_format.player_register_to_displayed(player2.__dict__), 0)]
        elif answer == "2":
            return [(self.manager_main.manager_format.player_register_to_displayed(player1.__dict__), 0),
                    (self.manager_main.manager_format.player_register_to_displayed(player2.__dict__), 1)]
        elif answer == "3":
            return [(self.manager_main.manager_format.player_register_to_displayed(player1.__dict__), 0.5),
                    (self.manager_main.manager_format.player_register_to_displayed(player2.__dict__), 0.5)]

    def save_result_match(self, match_instance):
        match_result = self.enter_result_match(match_instance.player1, match_instance.player2)
        self.manager_main.manager_insert.insert_result_match_to_match_to_database(
            match_instance.tournament_name, match_instance.round_name, match_instance.name, match_result)
        return match_result

    def select_match_without_result(list_match):
        list_match_need_result = []
        for match_inspected in list_match:
            if not match_inspected.result_match:
                list_match_need_result.append(match_inspected)
            else:
                pass
        return list_match_need_result

    select_match_without_result = staticmethod(select_match_without_result)

    def select_match_played(self, list_match):
        list_choice = []
        print(self.show_match.show_init_choice_match())
        for proposed_match in list_match:
            print(self.show_match.show_choice_match_to_change(proposed_match.round_name,
                                                              proposed_match, list_match.index(proposed_match)+1))
            list_choice.append(list_match.index(proposed_match)+1)
        answer = self.view_main.view_input.try_choice_input(list_choice)
        return list_match[int(answer)-1]

    def change_result_match(self, list_match):
        match_selected = self.select_match_played(list_match)
        print(self.show_match.confirm_result_match_register(self.save_result_match(match_selected)))

    def init_change_result_match(self, list_match):
        list_instance = self.replace_match_list_dict_to_instance(list_match)
        self.change_result_match(list_instance)

    def change_and_save_result_match(self, tournament_name):
        self.init_change_result_match(
            self.manager_main.check_main.check_models.open_load_all_matches_from_tournament(tournament_name))

    def register_result_match(self, list_match):
        match_selected = self.select_match_played(self.select_match_without_result(list_match))
        print(self.show_match.confirm_result_match_register(self.save_result_match(match_selected)))

    def show_result_match(self, list_match):
        for match in list_match:
            print(self.show_match.init_show_result_match(match.result_match))



"""
class ControlMatch:
    def __init__(self, manager):
        self.match = Match
        self.manager = manager

    def init_match(self, match_number, player1, player2):
        return self.match(match_number, player1, player2)

    def add_match(self, tournoi_number, round_number, match_number, player1, player2):
        self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match.append(self.init_match(
            match_number, player1, player2))

    # input result match
    def input_result_match(self, tournoi_number, round_number, match_number, result_player1, result_player2):
        self.match.result_match = (
            [self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match[match_number-1].player1,
             result_player1],
            [self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match[match_number-1].player2,
             result_player2])
        return self.match.result_match

    def add_result_match(self, tournoi_number, round_number, match_number, result_player1, result_player2):
        self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match[match_number-1].result_match = \
            self.input_result_match(tournoi_number, round_number, match_number, result_player1, result_player2)
"""