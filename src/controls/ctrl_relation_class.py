from src.controls.ctrl_player_methods import CtrlPlayerMethods
from src.controls.ctrl_tournament_methods import CtrlTournamentMethods
from src.controls.ctrl_tournament_running import CtrlTournamentRunning
from src.controls.ctrl_manager_main import CtrlManagerMain
from src.controls.ctrl_view_main import CtrlViewMain
from src.controls.ctrl_main_menu import CtrlMainMenu
from src.controls.ctrl_tournament_menu import CtrlTournamentMenu
from src.controls.ctrl_flake8 import CtrlPepHeight
from src.controls.ctrl_data_results import CtrlDataResults


class CtrlRelationClass:
    def __init__(self):
        self.view_main = CtrlViewMain()
        self.manager_main = CtrlManagerMain()
        self.flake_8 = CtrlPepHeight(self.view_main)
        self.player_methods = CtrlPlayerMethods(
            self.view_main, self.manager_main)
        self.tournament_methods = CtrlTournamentMethods(
            self.view_main, self.manager_main, self.player_methods)
        self.tournament_running = CtrlTournamentRunning(
            self.tournament_methods)
        self.data_results = CtrlDataResults(
            self.view_main, self.manager_main,
            self.player_methods, self.tournament_methods)
        self.main_menu = CtrlMainMenu(
            self.view_main, self.tournament_running,
            self.player_methods, self.flake_8, self.data_results)
        self.tournament_menu = CtrlTournamentMenu()


class LeaveApplication(Exception):
    def __init__(self):
        self.view_main = CtrlViewMain()
        self.manager_main = CtrlManagerMain()
        self.flake_8 = CtrlPepHeight(self.view_main)
        self.player_methods = CtrlPlayerMethods(
            self.view_main, self.manager_main)
        self.tournament_methods = CtrlTournamentMethods(
            self.view_main, self.manager_main, self.player_methods)
        self.data_results = CtrlDataResults(
            self.view_main, self.manager_main,
            self.player_methods, self.tournament_methods)
        self.main_menu = CtrlMainMenu(
            self.view_main, self.tournament_methods,
            self.player_methods, self.flake_8, self.data_results)

    def __str__(self):
        return self.main_menu.show_navigate_main_menu.show_leave_app()

    def __repr__(self):
        return self.__str__()


class LeaveTournament(Exception):
    def __init__(self, tournament_name):
        self.tournament_menu = CtrlTournamentMenu()
        self.tournament_name = tournament_name

    def __str__(self):
        return self.tournament_menu.quit_tournament(self.tournament_name)

    def __repr__(self):
        return self.__str__()
