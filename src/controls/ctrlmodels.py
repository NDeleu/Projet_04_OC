from src.models import Manager
from src.controls import ControlMatch
from src.controls import ControlRound
from src.controls import ControlTournoi
from src.controls import ControlPlayer
import datetime


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
ctrl.ctrl_player.add_player("Duflan", "Jack", 25, 2)
ctrl.ctrl_player.add_player("Dugratin", "Francis", 30, 3)
ctrl.ctrl_player.add_player("Duchoux", "Jean", 20, 5)
ctrl.ctrl_player.add_player("Delatarte", "Pierre", 40, 1)
ctrl.ctrl_player.add_player("Delacrepe", "Yves", 18, 4)
ctrl.ctrl_player.add_player("Dubouillon", "Brigitte", 60, 6)
ctrl.ctrl_player.add_player("Delagauffre", "Jose", 50, 8)
ctrl.ctrl_player.add_player("Dupoisson", "Nicolas", 32, 7)

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
"""
ctrl.ctrl_tournoi.start_tournoi(1)
ctrl.ctrl_tournoi.start_tournoi(1)
"""

print(ctrl.manager.list_all_tournoi[0].date)