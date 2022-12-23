import datetime

from src.models import Round
from src.models import Match
from src.models import Player
from src.models import Tournoi
from src.models import Manager

"""
# Round :

def first_round(self):
    sorted_by_rank = sorted(self.player_list, key=lambda x: x.rank)
    for y in range(int(len(sorted_by_rank) / 2)):
        self.match.append(
            MatchControl(y + 1, sorted_by_rank[y], sorted_by_rank[y + (int(len(sorted_by_rank) / 2))]))
        

# Round : arrangement des autres Rounds
def other_round(self):
    self.init_round_point_players(players)
    sorted_by_point = sorted(player_list, key=lambda x: x.round_point)
    for y in range(int(len(sorted_by_point) / 2)):
        round1.match.append(Match(y + 1, sorted_by_point[y], sorted_by_point[y + 1]))

 
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
        
        

    
"""


class ControlModels:
    def __init__(self):
        self.manager = Manager()
        self.ctrl_tournoi = ControlTournoi(self.manager)
        self.ctrl_player = ControlPlayer(self.manager)
        self.ctrl_round = ControlRound(self.manager)
        self.ctrl_match = ControlMatch(self.manager)


class ControlPlayer:
    def __init__(self, manager):
        self.player = Player
        self.manager = manager

    def init_player(self, name, surname, age, rank):
        return self.player(name, surname, age, rank)

    def add_player(self, name, surname, age, rank):
        self.manager.list_all_player.append(self.init_player(name, surname, age, rank))


class ControlTournoi:
    def __init__(self, manager):
        self.tournoi = Tournoi
        self.manager = manager

    def init_tournoi(self, name, lieu, player_list, control_temps, tours_round=4):
        return self.tournoi(name, lieu, player_list, control_temps, tours_round)

    def add_tournoi(self, name, lieu, player_list, control_temps, tours_round=4):
        self.manager.list_all_tournoi.append(self.init_tournoi(
            name, lieu, player_list, control_temps, tours_round))


class ControlRound:
    def __init__(self, manager):
        self.round = Round
        self.manager = manager

    def init_round(self, round_number):
        return self.round(round_number, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def add_round(self, tournoi_number, round_number):
        self.manager.list_all_tournoi[tournoi_number-1].round.append(self.init_round(round_number))


class ControlMatch:
    def __init__(self, manager):
        self.match = Match
        self.manager = manager

    def init_match(self, match_number, player1, player2):
        return self.match(match_number, player1, player2)

    def add_match(self, tournoi_number, round_number, match_number, player1, player2):
        self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match.append(self.init_match(
            match_number, player1, player2))

    # input result match

    def input_result_match(self, tournoi_number, round_number, match_number, result_player1, result_player2):
        self.match.result_match = (
            [self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match[match_number-1].player1,
             result_player1],
            [self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match[match_number-1].player2,
             result_player2])
        return self.match.result_match

    def add_result_match(self, tournoi_number, round_number, match_number, result_player1, result_player2):
        self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match[match_number-1] = \
            self.input_result_match(tournoi_number, round_number, match_number, result_player1, result_player2)

# For test :

# Création de l'instance de contrôle
ctrl = ControlModels()

# Ajout des joueurs dans la liste principale
ctrl.ctrl_player.add_player("Duflan", "Jack", 25, 2)
ctrl.ctrl_player.add_player("Dugratin", "Francis", 30, 3)
ctrl.ctrl_player.add_player("Duchoux", "Jean", 20, 5)
ctrl.ctrl_player.add_player("Delatarte", "Pierre", 40, 1)
ctrl.ctrl_player.add_player("Delacrepe", "Yves", 18, 4)
ctrl.ctrl_player.add_player("Dubouillon", "Brigitte", 60, 6)
ctrl.ctrl_player.add_player("Delagauffre", "Jose", 50, 8)
ctrl.ctrl_player.add_player("Dupoisson", "Nicolas", 32, 7)

# Création d'un Tournoi
ctrl.ctrl_tournoi.add_tournoi("Le grand tournoi", "Paris", ctrl.manager.list_all_player, "Blitz", 4)
ctrl.ctrl_round.add_round(1, 1)
ctrl.ctrl_match.add_match(1, 1, 1, ctrl.manager.list_all_player[0], ctrl.manager.list_all_player[1])
ctrl.ctrl_match.add_match(1, 1, 2, ctrl.manager.list_all_player[2], ctrl.manager.list_all_player[3])
ctrl.ctrl_match.add_result_match(1, 1, 1, 1, 0)
print(ctrl.manager.list_all_tournoi[0].round[0].match[0])
ctrl.ctrl_match.add_result_match(1, 1, 2, 0, 1)
print(ctrl.manager.list_all_tournoi[0].round[0].match[0], ctrl.manager.list_all_tournoi[0].round[0].match[1])

"""
# Création d'un Round dans Tournoi
ctrl_round.init_round(tournois_list[0].round, 1, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Création d'un Match dans Round dans Tournoi
ctrl_match.init_match(tournois_list[0].round[0].match, 1, pl1, pl2)
ctrl_match.init_match(tournois_list[0].round[0].match, 2, pl3, pl4)
"""

print(ctrl.manager.list_all_tournoi, ctrl.manager.list_all_tournoi[0].round,
      ctrl.manager.list_all_tournoi[0].round[0].match)

