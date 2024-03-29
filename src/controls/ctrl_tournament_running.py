
from src.controls import CtrlRoundMethods
from src.controls import LeaveRound
from src.controls import CtrlRoundRunning


class CtrlTournamentRunning:
    def __init__(self, tournament_methods):
        self.tournament_methods = tournament_methods
        self.copy = self.tournament_methods.copy
        self.round_methods = CtrlRoundMethods(
            self.tournament_methods.manager_main,
            self.tournament_methods.player_methods,
            self.tournament_methods.view_main,
            self.copy)
        self.round_running = CtrlRoundRunning(self.round_methods, self.copy)
        self.tournament_main = None
        self.tournament_main_running = True

    def tournament_run(self, tournament_name):
        if self.tournament_main_running is False:
            self.tournament_main_running = True
            return False

        else:

            self.tournament_main = self.tournament_methods.tournament(
                **self.tournament_methods.
                manager_main.check_main.check_models.open_load_tournament(
                    tournament_name))

            if not self.tournament_main.player_list:

                self.tournament_methods.no_player_in_list_player()

                answer_add_player = self.tournament_methods.\
                    init_choice_id_player_to_tournament()

                if answer_add_player is False:
                    self.tournament_main_running = False

                else:

                    self.tournament_main.player_list.append(
                        self.tournament_methods.player_methods.
                        id_player_to_inst_player_displayed(
                            self.tournament_methods.
                            choice_id_player_to_tournament(
                                answer_add_player,
                                self.tournament_main.player_list)))

                    self.tournament_methods.success_add_player()

                    self.tournament_methods.save_list_player_to_database(
                        self.tournament_main.name,
                        self.tournament_main.player_list)
            else:

                self.tournament_main.player_list = self.tournament_methods.\
                    replace_player_list_dict_to_instance(
                        self.tournament_main.player_list)

                if len(self.tournament_main.player_list) < 8:

                    self.tournament_methods.not_enough_player_in_list_player(
                        self.tournament_main.player_list)

                    answer_add_player = self.tournament_methods. \
                        init_choice_id_player_to_tournament()

                    if answer_add_player is False:
                        self.tournament_main_running = False

                    else:

                        self.tournament_main.player_list.append(
                            self.tournament_methods.player_methods.
                            id_player_to_inst_player_displayed(
                                self.tournament_methods.
                                choice_id_player_to_tournament(
                                    answer_add_player,
                                    self.tournament_main.player_list)))

                        self.tournament_methods.success_add_player()

                        self.tournament_methods.save_list_player_to_database(
                            self.tournament_main.name,
                            self.tournament_main.player_list)

                        if len(self.tournament_main.player_list) == 8:
                            self.tournament_methods.\
                                completed_player_in_list_player(
                                    self.tournament_main.player_list)

                else:

                    if not self.tournament_main.rounds:

                        self.tournament_main.rounds.append(
                            self.round_methods.
                            register_and_load_round_to_tournament(
                                "Round1", self.tournament_main.name))

                        self.round_methods.save_list_round_to_database(
                            self.tournament_main.name,
                            self.tournament_main.rounds)

                        if self.tournament_methods.update_date_start_round(
                                "Round1",
                                self.tournament_main.name,
                                self.tournament_main.date) is not None:
                            self.tournament_main.date.append(
                                self.tournament_methods.
                                update_date_start_round(
                                    "Round1",
                                    self.tournament_main.name,
                                    self.tournament_main.date))
                        else:
                            pass

                        self.tournament_methods.save_list_date_to_database(
                            self.tournament_main.name,
                            self.tournament_main.date)

                    else:

                        self.tournament_main.rounds = self.round_methods.\
                            replace_rounds_list_dict_to_instance(
                                self.tournament_main.rounds,
                                self.tournament_main.name)

                        if self.tournament_methods.manager_main.check_main.\
                                check_models.check_end_time_rounds_exists(
                                self.tournament_main.rounds[len(
                                    self.tournament_main.rounds) - 1].name,
                                self.tournament_main.name) is True:

                            if self.tournament_methods.update_date_end_round(
                                    self.tournament_main.rounds[len(
                                        self.tournament_main.rounds) - 1].name,
                                    self.tournament_main.name,
                                    self.tournament_main.date) is not None:
                                self.tournament_main.date.append(
                                    self.tournament_methods.
                                    update_date_end_round(
                                        self.tournament_main.rounds[len(
                                            self.tournament_main.rounds) - 1].
                                        name,
                                        self.tournament_main.name,
                                        self.tournament_main.date))

                                self.tournament_methods.\
                                    save_list_date_to_database(
                                        self.tournament_main.name,
                                        self.tournament_main.date)

                            else:

                                if int(len(self.tournament_main.rounds)) == \
                                        int(self.tournament_main.number_round):

                                    self.tournament_methods.end_tournament(
                                        self.tournament_main)

                                    self.tournament_methods.player_methods.\
                                        player_total_point_calculated(
                                            self.tournament_main.player_list)

                                    self.tournament_main_running = False

                                else:

                                    round_len_plus = \
                                        len(self.tournament_main.rounds) + 1
                                    self.tournament_main.rounds.append(
                                        self.round_methods.
                                        register_and_load_round_to_tournament(
                                            f"Round"
                                            f"{round_len_plus}",
                                            self.tournament_main.name))

                                    self.round_methods.\
                                        save_list_round_to_database(
                                            self.tournament_main.name,
                                            self.tournament_main.rounds)

                                    round_len = \
                                        len(self.tournament_main.rounds)
                                    if self.tournament_methods.\
                                            update_date_start_round(
                                            f"Round{round_len}",
                                            self.tournament_main.name,
                                            self.tournament_main.date) \
                                            is not None:
                                        self.tournament_main.date.append(
                                            self.tournament_methods.
                                            update_date_start_round(
                                                f"Round{round_len}",
                                                self.tournament_main.name,
                                                self.tournament_main.date))

                        else:
                            try:
                                self.tournament_methods.leave_rounds(
                                    self.round_running.round_run(
                                        f"Round"
                                        f"{len(self.tournament_main.rounds)}",
                                        self.tournament_main.name,
                                        self.tournament_main.player_list))
                            except LeaveRound:
                                self.tournament_main_running = False
