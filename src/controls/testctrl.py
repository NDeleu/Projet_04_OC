import datetime

from src.models import Round
from src.models import Match
from src.models import Player


player1 = Player("Duflan", "Jack", 25, 2)
player2 = Player("Dugratin", "Francis", 30, 3)
player3 = Player("Duchoux", "Jean", 20, 5)
player4 = Player("Delatarte", "Pierre", 40, 1)
player5 = Player("Delacrepe", "Yves", 18, 4)
player6 = Player("Dubouillon", "Brigitte", 60, 6)
player7 = Player("Delagauffre", "Jose", 50, 8)
player8 = Player("Dupoisson", "Nicolas", 32, 7)

player_list = [player1, player2, player3, player4, player5, player6, player7, player8]

round1 = Round(1, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# Round : initialise les instances de matchs dans round.match et print les matchs en question demandant un résultat
def init_round():
    for i in range(int(len(player_list) / 2)):
        round1.match.append(Match(i + 1, player_list[i], player_list[-1 - i]))
        print(round1.match[i])


# Round : print les matchs restant demandant un résultat
def show_match_to_record():
    for matching in round1.match:
        if not matching.result_match:
            print(matching)


# Round : Conditionne l'emploi des fonctions init et show en fonction du fait qu'init est déjà eu lieu ou non
def test_round():
    if not round1.match:
        init_round()
    else:
        show_match_to_record()


# Match : input result match
def input_result_match(match_number, result_player1, result_player2):
    return ([round1.match[match_number-1].player1, result_player1],
            [round1.match[match_number-1].player2, result_player2])


# Match : record result match
def record_result_match(match_number, result_player1, result_player2):
    round1.match[match_number-1].result_match = input_result_match(match_number, result_player1, result_player2)


test_round()

record_result_match(1, 1, 0)

test_round()
print(round1.match[0])



