import datetime
from src.models import Round


class ControlRound:
    def __init__(self, manager, match_control):
        self.round = Round
        self.manager = manager
        self.match_control = match_control

    def init_round(self, round_number):
        return self.round(round_number, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def add_round(self, tournoi_number, round_number):
        self.manager.list_all_tournoi[tournoi_number-1].round.append(self.init_round(round_number))

    # Round : print les matchs restants demandant un résultat
    def show_match_to_record(self, tournoi_number, round_number):
        for matching in self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            if not matching.result_match:
                print(matching)

    def first_round(self, tournoi_number, round_number):
        sorted_by_rank = sorted(self.manager.list_all_tournoi[tournoi_number-1].player_list, key=lambda x: x.rank)
        for y in range(int(len(sorted_by_rank) / 2)):
            self.match_control.add_match(
                tournoi_number, round_number, y + 1, sorted_by_rank[y],
                sorted_by_rank[y + (int(len(sorted_by_rank) / 2))])

    # Round : initialise les instances de matchs dans round.match et print les matchs en question demandant un résultat
    def run_round(self, tournoi_number, round_number):
        self.first_round(tournoi_number, round_number)

    # Round : Conditionne l'emploi des fonctions init et show en fonction du fait qu'init est déjà eu lieu ou non
    def test_round(self, tournoi_number, round_number):
        if not self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            self.run_round(tournoi_number, round_number)
            self.show_match_to_record(tournoi_number, round_number)
        else:
            self.show_match_to_record(tournoi_number, round_number)
