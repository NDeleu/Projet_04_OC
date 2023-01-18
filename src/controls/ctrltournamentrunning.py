from src.controls.ctrlroundrunning import CtrlRoundRunning
from src.controls.ctrlroundmethods import CtrlRoundMethods


class CtrlTournamentRunning:
    def __init__(self):
        self.round_methods = CtrlRoundMethods()
        self.round_running = CtrlRoundRunning()
