from src.controls import CtrlManagerCheckResults
from src.controls import CtrlManagerCheckModels


class CtrlManagerCheckMain:
    def __init__(self, manager):
        self.manager_to_check_main = manager
        self.check_results = CtrlManagerCheckResults(
            self.manager_to_check_main)
        self.check_models = CtrlManagerCheckModels(
            self.manager_to_check_main)
