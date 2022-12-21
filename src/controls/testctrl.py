import datetime

from src.models import Round
from src.models import Match
from src.models import Player


class RoundControl(Round):
    def __init__(self, player_list, round_number, start_time):
        super().__init__(round_number, start_time)
        self.player_list = player_list

    # Round : arrangement du Premier Round
    def first_round(self):
        sorted_by_rank = sorted(self.player_list, key=lambda x: x.rank)
        for y in range(int(len(sorted_by_rank) / 2)):
            self.match.append(
                MatchControl(y + 1, sorted_by_rank[y], sorted_by_rank[y + (int(len(sorted_by_rank) / 2))]))

    """
    # Round : arrangement des autres Rounds
    def other_round(self):
        self.init_round_point_players(players)
        sorted_by_point = sorted(player_list, key=lambda x: x.round_point)
        for y in range(int(len(sorted_by_point) / 2)):
            round1.match.append(Match(y + 1, sorted_by_point[y], sorted_by_point[y + 1]))
    """

    # les deux prochaines methodes de round point seront pr la class TournoiControl, et non pas pour
    # RoundControl. Il faudra aussi veiller à ne pas considérer les matchs du round en cours pr éviter
    # les probs si on load une game ac un round en cours, à réfléchir...
    def init_round_point_players(self):
        for player in self.player_list:
            self.round_point_player(player)

    def round_point_player(self, player):
        player.round_point = 0
        # for matchs in rounds:
        for matching in self.match:
            if matching.result_match:
                if player == matching.result_match[0][0]:
                    player.round_point += matching.result_match[0][1]
                elif player == matching.result_match[1][0]:
                    player.round_point += matching.result_match[1][1]

    def init_encountered_player(self):
        for player in self.player_list:
            self.encountered_player(player)

    def encountered_player(self, player):
        player.encountered.clear()
        # for matchs in rounds:
        for matching in self.match:
            if matching.result_match:
                if player == matching.result_match[0][0]:
                    player.encountered.append(matching.result_match[1][0])
                elif player == matching.result_match[1][0]:
                    player.encountered.append(matching.result_match[0][0])

    # Round : initialise les instances de matchs dans round.match et print les matchs en question demandant un résultat
    def init_round(self):
        self.first_round()

    # Round : print les matchs restants demandant un résultat
    def show_match_to_record(self):
        for matching in self.match:
            if not matching.result_match:
                print(matching)

    # Round : Conditionne l'emploi des fonctions init et show en fonction du fait qu'init est déjà eu lieu ou non
    def test_round(self):
        if not self.match:
            self.init_round()
            self.show_match_to_record()
        else:
            self.show_match_to_record()


class MatchControl(Match):
    def __init__(self, match_number, player1, player2):
        super().__init__(match_number, player1, player2)

    # Match : input result match
    def input_result_match(self, result_player1, result_player2):
        return [self.player1, result_player1], [self.player2, result_player2]

    # Match : record result match
    def record_result_match(self, result_player1, result_player2):
        self.result_match = (self.input_result_match(result_player1, result_player2))


# Les éléments qui suit seront implantés dans Round à partir de Tournoi
# mise en place des joueurs
pl1 = Player("Duflan", "Jack", 25, 2)
pl2 = Player("Dugratin", "Francis", 30, 3)
pl3 = Player("Duchoux", "Jean", 20, 5)
pl4 = Player("Delatarte", "Pierre", 40, 1)
pl5 = Player("Delacrepe", "Yves", 18, 4)
pl6 = Player("Dubouillon", "Brigitte", 60, 6)
pl7 = Player("Delagauffre", "Jose", 50, 8)
pl8 = Player("Dupoisson", "Nicolas", 32, 7)

list_play = [pl1, pl2, pl3, pl4, pl5, pl6, pl7, pl8]

round1 = RoundControl(list_play, 1, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print(pl4.encountered)

round1.test_round()
round1.match[0].record_result_match(1, 0)
print(round1.match[0])
round1.init_encountered_player()
print(pl4.encountered)

"""
print(round1)
print(round1.match)
round1.test_round()

round1.match[0].record_result_match(1, 0)

round1.test_round()
print(round1.match[0])

round1.match[1].record_result_match(0, 1)

round1.test_round()
print(round1.match[1])
"""



