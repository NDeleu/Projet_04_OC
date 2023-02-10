from src.models import Manager
from src.controls import CtrlManagerCheckMain
from src.controls import CtrlManagerFormat
from src.controls import CtrlManagerInsert


class CtrlManagerMain:
    def __init__(self):
        self.manager = Manager()
        self.check_main = CtrlManagerCheckMain(self.manager)
        self.manager_format = CtrlManagerFormat(self.manager)
        self.manager_insert = CtrlManagerInsert(self.manager)
