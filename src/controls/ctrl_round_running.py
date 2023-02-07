import copy

from src.controls.ctrl_match_methods import CtrlMatchMethods


class CtrlRoundRunning:
    def __init__(self, round_methods):
        self.round_methods = round_methods
        self.match_methods = CtrlMatchMethods(
            self.round_methods.manager_main,
            self.round_methods.player_methods,
            self.round_methods.view_main)
        self.round_main = None
        self.round_main_running = True
        self.player_list = None

    def round_run(self, round_name, tournament_name, list_player):
        if self.round_main_running is False:
            self.round_main_running = True
            return False
        else:

            self.round_main = self.round_methods.round_registered(
                **self.round_methods.manager_main.check_main.
                check_models.open_load_rounds(round_name, tournament_name))

            self.player_list = copy.deepcopy(list_player)

            if not self.round_main.match:

                self.round_methods.show_create_round(self.round_main.name)

                if self.round_main.name == "Round1":

                    for y in self.round_methods.init_first_round(
                            self.player_list):
                        self.round_main.match.append(
                            self.match_methods.
                            register_and_load_match_to_round(
                                f"Match{y[0]}",
                                self.round_main.name,
                                self.round_main.tournament_name,
                                y[1][0],
                                y[1][1]))

                    self.match_methods.save_list_match_to_database(
                        self.round_main.tournament_name,
                        self.round_main.name,
                        self.round_main.match)

                else:

                    for y in self.round_methods.init_other_round(
                            self.round_main.tournament_name, self.player_list):
                        self.round_main.match.append(
                            self.match_methods.
                            register_and_load_match_to_round(
                                f"Match{y[0]}",
                                self.round_main.name,
                                self.round_main.tournament_name,
                                y[1][0],
                                y[1][1]))

                    self.match_methods.save_list_match_to_database(
                        self.round_main.tournament_name,
                        self.round_main.name,
                        self.round_main.match)

            else:

                self.round_main.match = self.match_methods.\
                    replace_match_list_dict_to_instance(
                        self.round_main.match)

                self.round_methods.resume_round(self.round_main.name)

                if self.round_methods.check_all_match_played(
                        self.round_main.match) is True:
                    pass
                    self.round_methods.show_end_round(self.round_main.name)
                    self.match_methods.show_result_match(self.round_main.match)
                    self.round_methods.add_end_time_round(
                        self.round_main.tournament_name, self.round_main.name)

                else:
                    self.match_methods.register_result_match(
                        self.round_main.match)

            self.round_main_running = self.round_methods.round_keep_running()
