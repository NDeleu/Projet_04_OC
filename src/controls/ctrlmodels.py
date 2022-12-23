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
        self.ctrl_tournoi = ControlTournoi(self.manager)
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
ctrl.ctrl_tournoi.add_tournoi("Le grand tournoi", "Paris", ctrl.manager.list_all_player, "Blitz", 4)
ctrl.ctrl_round.add_round(1, 1)

"""
ctrl.ctrl_match.add_match(1, 1, 1, ctrl.manager.list_all_player[0], ctrl.manager.list_all_player[1])
ctrl.ctrl_match.add_match(1, 1, 2, ctrl.manager.list_all_player[2], ctrl.manager.list_all_player[3])
ctrl.ctrl_match.add_match(1, 1, 3, ctrl.manager.list_all_player[4], ctrl.manager.list_all_player[5])
ctrl.ctrl_match.add_match(1, 1, 4, ctrl.manager.list_all_player[6], ctrl.manager.list_all_player[7])
"""
ctrl.ctrl_round.test_round(1, 1)
print(ctrl.manager.list_all_tournoi[0].round[0].match)

"""
ctrl.ctrl_match.add_result_match(1, 1, 1, 1, 0)
print(ctrl.manager.list_all_tournoi[0].round[0].match[0])
ctrl.ctrl_match.add_result_match(1, 1, 2, 0, 1)
print(ctrl.manager.list_all_tournoi[0].round[0].match[0], ctrl.manager.list_all_tournoi[0].round[0].match[1])

print(ctrl.manager.list_all_tournoi, ctrl.manager.list_all_tournoi[0].round,
      ctrl.manager.list_all_tournoi[0].round[0].match)
"""
ctrl.ctrl_round.show_match_to_record(1, 1)

