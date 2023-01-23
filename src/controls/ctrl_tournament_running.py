from src.controls.ctrl_round_running import CtrlRoundRunning
from src.controls.ctrl_round_methods import CtrlRoundMethods


class CtrlTournamentRunning:
    def __init__(self):
        self.round_methods = CtrlRoundMethods()
        self.round_running = CtrlRoundRunning()
