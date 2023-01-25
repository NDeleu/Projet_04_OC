from src.controls.ctrl_round_running import CtrlRoundRunning
from src.controls.ctrl_round_methods import CtrlRoundMethods


class CtrlTournamentRunning:
    def __init__(self, tournament_methods):
        self.round_methods = CtrlRoundMethods()
        self.round_running = CtrlRoundRunning()
        self.tournament_methods = tournament_methods
        self.tournament_main = None
        self.tournament_main_running = True

    def tournament_run(self, tournament_name):
        if self.tournament_main_running is False:
            return False
        else:

            self.tournament_main = self.tournament_methods.tournament(**
                                                                      self.tournament_methods.manager_main.check_main.
                                                                      check_models.open_load_tournament(tournament_name))
            print("name : ", self.tournament_main.name)
            print("lieu : ", self.tournament_main.location)
            print("nombre de round : ", self.tournament_main.number_round)

            self.tournament_main_running = self.tournament_methods.tournament_keep_running()
