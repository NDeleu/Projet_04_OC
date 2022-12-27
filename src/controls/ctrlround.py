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

    def other_round(self, tournoi_number, round_number):
        sorted_by_round_point = sorted(
            self.manager.list_all_tournoi[tournoi_number-1].player_list, key=lambda x: x.round_point)
        for y in range(int(len(sorted_by_round_point) / 2)):
            self.match_control.add_match(
                tournoi_number, round_number, y + 1,
                self.test_player1_matches_round(sorted_by_round_point, tournoi_number, round_number),
                self.test_player2_matches_round(sorted_by_round_point, tournoi_number, round_number))

    # Vérifie si la liste match de ce round existe
    def test_player1_matches_round(self, list_played, tournoi_number, round_number):
        if self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            return self.test_player1_in_round(list_played, tournoi_number, round_number)
        else:
            return list_played[0]

    # Vérifie si le joueur est déjà dans un match du round
    def test_player1_in_round(self, list_played, tournoi_number, round_number):
        for player in list_played:
            if self.test_player_in_round_incept(player, tournoi_number, round_number) is False:
                pass
            else:
                return player

    def test_player2_matches_round(self, list_played, tournoi_number, round_number):
        if self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            return self.test_player2_in_round(list_played, tournoi_number, round_number)
        else:
            for player in list_played:
                if player == self.test_player1_matches_round(list_played, tournoi_number, round_number):
                    pass
                elif player in self.test_player1_matches_round(list_played, tournoi_number, round_number).encountered:
                    pass      
                else:
                    return player

    def test_player2_in_round(self, list_played, tournoi_number, round_number):
        for player in list_played:
            if self.test_player_in_round_incept(player, tournoi_number, round_number) is False:
                pass
            elif player == self.test_player1_matches_round(list_played, tournoi_number, round_number):
                pass
            elif player in self.test_player1_matches_round(list_played, tournoi_number, round_number).encountered:
                pass
            else:
                return player

    def test_player_in_round_incept(self, player, tournoi_number, round_number):
        for matching in self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            if player == matching.player1 or player == matching.player2:
                return False

    def init_round_point(self, tournoi_number):
        for player in self.manager.list_all_tournoi[tournoi_number-1].player_list:
            player.round_point = 0
            self.calcul_round_point(tournoi_number, player)

    def calcul_round_point(self, tournoi_number, player):
        for rounding in self.manager.list_all_tournoi[tournoi_number-1].round:
            for matching in rounding.match:
                if player == matching.result_match[0][0]:
                    player.round_point += matching.result_match[0][1]
                elif player == matching.result_match[1][0]:
                    player.round_point += matching.result_match[1][1]

    # Round : initialise les instances de matchs dans round.match et print les matchs en question demandant un résultat
    def run_round(self, tournoi_number, round_number):
        if round_number == 1:
            self.first_round(tournoi_number, round_number)
        else:
            self.other_round(tournoi_number, round_number)

    # Round : Conditionne l'emploi des fonctions init et show en fonction du fait qu'init est déjà eu lieu ou non
    def test_round(self, tournoi_number, round_number):
        if not self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            self.init_round_point(tournoi_number)
            self.run_round(tournoi_number, round_number)
            self.show_match_to_record(tournoi_number, round_number)
        else:
            self.show_match_to_record(tournoi_number, round_number)
