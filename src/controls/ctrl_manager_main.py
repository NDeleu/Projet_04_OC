from src.models.mdl_manager import Manager
from src.controls.ctrl_manager_check_main import CtrlManagerCheckMain
from src.controls.ctrl_manager_format import CtrlManagerFormat
from src.controls.ctrl_manager_insert import CtrlManagerInsert


class CtrlManagerMain:
    def __init__(self):
        self.manager = Manager()
        self.check_main = CtrlManagerCheckMain(self.manager)
        self.manager_format = CtrlManagerFormat(self.manager)
        self.manager_insert = CtrlManagerInsert(self.manager)
