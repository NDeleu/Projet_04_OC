from src.controls.ctrlplayermethods import CtrlPlayerMethods
from src.controls.ctrltournamentmethods import CtrlTournamentMethods
from src.controls.ctrltournamentrunning import CtrlTournamentRunning
from src.controls.ctrlmanagermain import CtrlManagerMain
from src.controls.ctrlviewmain import CtrlViewMain
from src.controls.ctrlmainmenu import CtrlMainMenu
from src.controls.ctrltournamentmenu import CtrlTournamentMenu


class CtrlRelationClass:
    def __init__(self):
        self.player_methods = CtrlPlayerMethods()
        self.tournament_methods = CtrlTournamentMethods()
        self.tournament_running = CtrlTournamentRunning()
        self.manager_main = CtrlManagerMain
        self.view_main = CtrlViewMain()
        self.main_menu = CtrlMainMenu()
        self.tournament_menu = CtrlTournamentMenu

