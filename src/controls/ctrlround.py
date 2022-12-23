import datetime
from src.models import Round


class ControlRound:
    def __init__(self, manager):
        self.round = Round
        self.manager = manager

    def init_round(self, round_number):
        return self.round(round_number, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def add_round(self, tournoi_number, round_number):
        self.manager.list_all_tournoi[tournoi_number-1].round.append(self.init_round(round_number))
