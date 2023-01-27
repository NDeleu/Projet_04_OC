import copy

from src.controls.ctrl_match_methods import CtrlMatchMethods


class CtrlRoundRunning:
    def __init__(self, round_methods):
        self.match_methods = CtrlMatchMethods()
        self.round_methods = round_methods
        self.round_main = None
        self.round_main_running = True
        self.player_list = None

    def round_run(self, round_name, tournament_name, list_player):
        if self.round_main_running is False:
            return False
        else:

            self.round_main = self.round_methods.round_registered(**
                                                                  self.round_methods.manager_main.check_main.
                                                                  check_models.open_load_rounds(
                                                                      round_name, tournament_name))

        self.player_list = copy.deepcopy(list_player)
        print(self.player_list)
        print(self.round_main.name)
        print(self.round_main.tournament_name)

        """
        if not round_main.match:
            self.round_methods.creat_matches...avec choix si premier round ou autre (round_name, list_player)
        else:
            if round_main.match... a tous les resultats (sont tous joués):
                add end time
            else:
                proposer d'insérer les résultats des matchs
        """
        self.round_main_running = self.round_methods.round_keep_running()
