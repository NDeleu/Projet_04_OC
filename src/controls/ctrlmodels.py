from src.controls import ControlManager
from src.controls import ControlMatch
from src.controls import ControlRound
from src.controls import ControlTournoi
from src.controls import ControlPlayer


class ControlModels:
    def __init__(self):
        self.ctrl_manager = ControlManager()
        self.ctrl_player = ControlPlayer(self.ctrl_manager)
        self.ctrl_match = ControlMatch(self.ctrl_manager)
        self.ctrl_round = ControlRound(self.ctrl_manager, self.ctrl_match)
        self.ctrl_tournoi = ControlTournoi(self.ctrl_manager, self.ctrl_round)


# For test :

# Création de l'instance de contrôle
ctrl = ControlModels()

"""
# Ajout des joueurs dans la liste principale
ctrl.ctrl_player.add_player("Duflan", "Jack", "01/01/1980", "AB12345")
ctrl.ctrl_player.add_player("Dugratin", "Francis", "01/03/1985", "BB12345")
ctrl.ctrl_player.add_player("Duchoux", "Jean", "15/01/1990", "CB12345")
ctrl.ctrl_player.add_player("Delatarte", "Pierre", "25/05/1970", "DB12345")
ctrl.ctrl_player.add_player("Delacrepe", "Yves", "01/05/2001", "EB12345")
ctrl.ctrl_player.add_player("Dubouillon", "Brigitte", "01/01/1960", "FB12345")
ctrl.ctrl_player.add_player("Delagauffre", "Jose", "05/12/1975", "GB12345")
ctrl.ctrl_player.add_player("Dupoisson", "Nicolas", "02/01/1983", "HB12345")
"""
"""
ctrl.ctrl_player.load_player(1)
ctrl.ctrl_player.load_player(2)
ctrl.ctrl_player.load_player(3)
ctrl.ctrl_player.load_player(4)
ctrl.ctrl_player.load_player(5)
ctrl.ctrl_player.load_player(6)
ctrl.ctrl_player.load_player(7)
ctrl.ctrl_player.load_player(8)


# Création d'un Tournoi
ctrl.ctrl_tournoi.add_tournoi("Le grand tournoi", "Paris", "Blitz", 4)

# ajout des joueurs dans le tournoi
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.ctrl_manager.list_all_player[0])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.ctrl_manager.list_all_player[1])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.ctrl_manager.list_all_player[2])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.ctrl_manager.list_all_player[3])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.ctrl_manager.list_all_player[4])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.ctrl_manager.list_all_player[5])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.ctrl_manager.list_all_player[6])
ctrl.ctrl_tournoi.add_player_tournoi(1, ctrl.ctrl_manager.list_all_player[7])

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
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.ctrl_manager.list_all_player[0])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.ctrl_manager.list_all_player[1])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.ctrl_manager.list_all_player[2])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.ctrl_manager.list_all_player[3])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.ctrl_manager.list_all_player[4])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.ctrl_manager.list_all_player[5])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.ctrl_manager.list_all_player[6])
ctrl.ctrl_tournoi.add_player_tournoi(2, ctrl.ctrl_manager.list_all_player[7])

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
ctrl.ctrl_tournoi.start_tournoi(1)

print(ctrl.ctrl_manager.list_all_tournoi)


# a placer à l open et a la save du player ? on retire l init et on insere le nom du joueur direct ?
ctrl.ctrl_player.init_total_point()

print(ctrl.ctrl_manager.list_all_player[0], ctrl.ctrl_manager.list_all_player[0].total_point)
print(ctrl.ctrl_manager.list_all_player[1], ctrl.ctrl_manager.list_all_player[1].total_point)
print(ctrl.ctrl_manager.list_all_player[2], ctrl.ctrl_manager.list_all_player[2].total_point)

for players in ctrl.ctrl_manager.list_all_player:
    ctrl.ctrl_manager.save_player_to_json((ctrl.ctrl_manager.manager.db_players.get(ctrl.ctrl_manager.manager.seek.identifiant == players.identifiant)).doc_id)
"""

print(ctrl.ctrl_manager.list_all_player)
ctrl.ctrl_player.load_all_player()
print(ctrl.ctrl_manager.list_all_player)
