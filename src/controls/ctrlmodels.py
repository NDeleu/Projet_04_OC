from src.models import Manager
from src.controls import ControlMatch
from src.controls import ControlRound
from src.controls import ControlTournoi
from src.controls import ControlPlayer


class ControlModels:
    def __init__(self):
        self.manager = Manager()
        self.ctrl_match = ControlMatch(self.manager)
        self.ctrl_round = ControlRound(self.manager, self.ctrl_match)
        self.ctrl_tournoi = ControlTournoi(self.manager, self.ctrl_round)
        self.ctrl_player = ControlPlayer(self.manager)


# For test :

# Création de l'instance de contrôle
ctrl = ControlModels()

# Ajout des joueurs dans la liste principale
ctrl.ctrl_player.add_player("Duflan", "Jack", "01/01/1980", "AB12345")
ctrl.ctrl_player.add_player("Dugratin", "Francis", "01/03/1985", "BB12345")
ctrl.ctrl_player.add_player("Duchoux", "Jean", "15/01/1990", "CB12345")
ctrl.ctrl_player.add_player("Delatarte", "Pierre", "25/05/1970", "DB12345")
ctrl.ctrl_player.add_player("Delacrepe", "Yves", "01/05/2001", "EB12345")
ctrl.ctrl_player.add_player("Dubouillon", "Brigitte", "01/01/1960", "FB12345")
ctrl.ctrl_player.add_player("Delagauffre", "Jose", "05/12/1975", "GB12345")
ctrl.ctrl_player.add_player("Dupoisson", "Nicolas", "02/01/1983", "HB12345")

# Création d'un Tournoi
ctrl.ctrl_tournoi.add_tournoi("Le grand tournoi", "Paris", "Blitz", 4)

# ajout des joueurs dans le tournoi
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.manager.list_all_player[0])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.manager.list_all_player[1])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.manager.list_all_player[2])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.manager.list_all_player[3])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.manager.list_all_player[4])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.manager.list_all_player[5])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.manager.list_all_player[6])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.manager.list_all_player[7])

ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)

ctrl.ctrl_match.add_result_match(1, 1, 1, 1, 0)

ctrl.ctrl_tournoi.start_tournoi(1)

ctrl.ctrl_match.add_result_match(1, 1, 2, 1, 0)
ctrl.ctrl_match.add_result_match(1, 1, 3, 0.5, 0.5)
ctrl.ctrl_match.add_result_match(1, 1, 4, 0, 1)

ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)

ctrl.ctrl_match.add_result_match(1, 2, 1, 1, 0)
ctrl.ctrl_match.add_result_match(1, 2, 2, 1, 0)
ctrl.ctrl_match.add_result_match(1, 2, 3, 0.5, 0.5)
ctrl.ctrl_match.add_result_match(1, 2, 4, 0, 1)

ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)

ctrl.ctrl_match.add_result_match(1, 3, 1, 1, 0)
ctrl.ctrl_match.add_result_match(1, 3, 2, 1, 0)
ctrl.ctrl_match.add_result_match(1, 3, 3, 0.5, 0.5)
ctrl.ctrl_match.add_result_match(1, 3, 4, 0, 1)

ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)

ctrl.ctrl_match.add_result_match(1, 4, 1, 1, 0)
ctrl.ctrl_match.add_result_match(1, 4, 2, 1, 0)
ctrl.ctrl_match.add_result_match(1, 4, 3, 0.5, 0.5)
ctrl.ctrl_match.add_result_match(1, 4, 4, 0, 1)

ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)

# Création d'un second tournoi

# Création d'un Tournoi
ctrl.ctrl_tournoi.add_tournoi("Le petit tournoi", "Bretz", "Blitz", 4)

# ajout des joueurs dans le tournoi
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.manager.list_all_player[0])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.manager.list_all_player[1])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.manager.list_all_player[2])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.manager.list_all_player[3])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.manager.list_all_player[4])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.manager.list_all_player[5])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.manager.list_all_player[6])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.manager.list_all_player[7])

ctrl.ctrl_tournoi.start_tournoi(2)
ctrl.ctrl_tournoi.start_tournoi(2)

ctrl.ctrl_match.add_result_match(2, 1, 1, 1, 0)

ctrl.ctrl_tournoi.start_tournoi(2)

ctrl.ctrl_match.add_result_match(2, 1, 2, 1, 0)
ctrl.ctrl_match.add_result_match(2, 1, 3, 0.5, 0.5)
ctrl.ctrl_match.add_result_match(2, 1, 4, 0, 1)

ctrl.ctrl_tournoi.start_tournoi(2)
ctrl.ctrl_tournoi.start_tournoi(2)
ctrl.ctrl_tournoi.start_tournoi(2)

ctrl.ctrl_match.add_result_match(2, 2, 1, 1, 0)
ctrl.ctrl_match.add_result_match(2, 2, 2, 1, 0)
ctrl.ctrl_match.add_result_match(2, 2, 3, 0.5, 0.5)
ctrl.ctrl_match.add_result_match(2, 2, 4, 0, 1)

ctrl.ctrl_tournoi.start_tournoi(2)
ctrl.ctrl_tournoi.start_tournoi(2)
ctrl.ctrl_tournoi.start_tournoi(2)

ctrl.ctrl_match.add_result_match(2, 3, 1, 1, 0)
ctrl.ctrl_match.add_result_match(2, 3, 2, 1, 0)
ctrl.ctrl_match.add_result_match(2, 3, 3, 0.5, 0.5)
ctrl.ctrl_match.add_result_match(2, 3, 4, 0, 1)

ctrl.ctrl_tournoi.start_tournoi(2)
ctrl.ctrl_tournoi.start_tournoi(2)
ctrl.ctrl_tournoi.start_tournoi(2)

ctrl.ctrl_match.add_result_match(2, 4, 1, 1, 0)
ctrl.ctrl_match.add_result_match(2, 4, 2, 1, 0)
ctrl.ctrl_match.add_result_match(2, 4, 3, 0.5, 0.5)
ctrl.ctrl_match.add_result_match(2, 4, 4, 0, 1)

ctrl.ctrl_tournoi.start_tournoi(2)
ctrl.ctrl_tournoi.start_tournoi(2)
ctrl.ctrl_tournoi.start_tournoi(2)
ctrl.ctrl_tournoi.start_tournoi(2)

print(ctrl.manager.list_all_tournoi)


# total points joueurs à mettre a jour each time
def calcul_total_point(players):
    for tournoi in ctrl.manager.list_all_tournoi:
        for rounding in tournoi.round:
            for matching in rounding.match:
                if players == matching.result_match[0][0]:
                    players.total_point += matching.result_match[0][1]
                elif players == matching.result_match[1][0]:
                    players.total_point += matching.result_match[1][1]

def init_total_point(players):
    for players in ctrl.manager.list_all_player:
        players.total_point = 0
        calcul_total_point(players)


for players in ctrl.manager.list_all_player:
    init_total_point(players)

print(ctrl.manager.list_all_player[0], ctrl.manager.list_all_player[0].total_point)
