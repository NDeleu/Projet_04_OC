from src.controls import CtrlPlayerMethods, CtrlTournamentMethods, CtrlTournamentRunning, CtrlManagerMain, \
    CtrlViewMain, CtrlMainMenu, CtrlTournamentMenu


class CtrlRelationClass:
    def __init__(self):
        self.player_methods = CtrlPlayerMethods
        self.tournament_methods = CtrlTournamentMethods
        self.tournament_running = CtrlTournamentRunning
        self.manager_main = CtrlManagerMain
        self.view_main = CtrlViewMain
        self.main_menu = CtrlMainMenu
        self.tournament_menu = CtrlTournamentMenu


"""
class ControlModels:
    def __init__(self):
        self.ctrl_manager = ControlManager()
        self.ctrl_player = ControlPlayer(self.ctrl_manager)
        self.ctrl_match = ControlMatch(self.ctrl_manager)
        self.ctrl_round = ControlRound(self.ctrl_manager, self.ctrl_match)
        self.ctrl_tournoi = ControlTournoi(self.ctrl_manager, self.ctrl_round, self.ctrl_player)
"""