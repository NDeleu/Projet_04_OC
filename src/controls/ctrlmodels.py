from src.controls import ControlManager
from src.controls import ControlMatch
from src.controls import ControlRound
from src.controls import ControlTournoi
from src.controls import ControlPlayer
# from pprint import pprint


class ControlModels:
    def __init__(self):
        self.ctrl_manager = ControlManager()
        self.ctrl_player = ControlPlayer(self.ctrl_manager)
        self.ctrl_match = ControlMatch(self.ctrl_manager)
        self.ctrl_round = ControlRound(self.ctrl_manager, self.ctrl_match)
        self.ctrl_tournoi = ControlTournoi(self.ctrl_manager, self.ctrl_round, self.ctrl_player)


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


"""
# Chargement des joueurs dans la liste principale
ctrl.ctrl_player.load_player_by_idplayer("AB12345")
ctrl.ctrl_player.load_player_by_idplayer("BB12345")
ctrl.ctrl_player.load_player_by_idplayer("CB12345")
ctrl.ctrl_player.load_player_by_idplayer("DB12345")
ctrl.ctrl_player.load_player_by_idplayer("EB12345")
ctrl.ctrl_player.load_player_by_idplayer("FB12345")
ctrl.ctrl_player.load_player_by_idplayer("GB12345")
ctrl.ctrl_player.load_player_by_idplayer("HB12345")
"""


# Création d'un Tournoi
ctrl.ctrl_tournoi.add_tournoi("Le grand tournoi", "Paris", "Blitz", 4)


"""
# chargement de tous les joueurs
ctrl.ctrl_player.load_all_player()
"""

"""
# Chargement d'un Tournoi
ctrl.ctrl_tournoi.load_tournoi_by_name("Le grand tournoi")
"""


# chargement et ajout des joueurs dans le tournoi
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "AB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "BB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "CB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "DB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "EB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "FB12345")
# création et ajout des joueurs dans le tournoi
ctrl.ctrl_tournoi.creat_add_player_tournoi(1, "Delagauffre", "Jose", "05/12/1975", "GB12345")
ctrl.ctrl_tournoi.creat_add_player_tournoi(1, "Dupoisson", "Nicolas", "02/01/1983", "HB12345")

ctrl.ctrl_manager.save_players_tournoi_to_json(1)


# Lancement du tournoi
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

# Création d'un second tournoi

# Création d'un Tournoi
ctrl.ctrl_tournoi.add_tournoi("Le petit tournoi", "Bretz", "Blitz", 4)

# ajout des joueurs dans le tournoi
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "AB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "BB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "CB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "DB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "EB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "FB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "GB12345")
ctrl.ctrl_tournoi.load_add_player_tournoi(1, "HB12345")

ctrl.ctrl_manager.save_players_tournoi_to_json(1)

# lancement du tournoi
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

ctrl.ctrl_player.load_all_player()
print(ctrl.ctrl_manager.list_all_player)
ctrl.ctrl_tournoi.load_all_tournoi()
print(ctrl.ctrl_manager.list_all_tournoi)
for tournoi in ctrl.ctrl_manager.list_all_tournoi:
    print(tournoi.player_list)
ctrl.ctrl_player.init_total_point()
print(ctrl.ctrl_manager.list_all_player[0], ctrl.ctrl_manager.list_all_player[0].total_point)
print(ctrl.ctrl_manager.list_all_player[1], ctrl.ctrl_manager.list_all_player[1].total_point)
print(ctrl.ctrl_manager.list_all_player[2], ctrl.ctrl_manager.list_all_player[2].total_point)
print(ctrl.ctrl_manager.list_all_player[3], ctrl.ctrl_manager.list_all_player[3].total_point)
print(ctrl.ctrl_manager.list_all_player[4], ctrl.ctrl_manager.list_all_player[4].total_point)
print(ctrl.ctrl_manager.list_all_player[5], ctrl.ctrl_manager.list_all_player[5].total_point)
print(ctrl.ctrl_manager.list_all_player[6], ctrl.ctrl_manager.list_all_player[6].total_point)
print(ctrl.ctrl_manager.list_all_player[7], ctrl.ctrl_manager.list_all_player[7].total_point)
"""
# chargement de tous les tournois en vu de les afficher puis clear
ctrl.ctrl_tournoi.load_all_tournoi()
print(ctrl.ctrl_manager.list_all_tournoi)
ctrl.ctrl_manager.clear_list_tournoi()
"""

"""
# chargement de tous les joueurs en vu d'afficher leurs scores puis clear
ctrl.ctrl_player.load_all_player()
for player in sorted(ctrl.ctrl_manager.list_all_player,
                     key=lambda x: x.total_point, reverse=True):
    print(player, " ", player.total_point, "points")
ctrl.ctrl_manager.clear_list_player()
"""

"""
# Afficher la base de données des joueurs
for joueurs in ctrl.ctrl_manager.manager.db_players: 
    pprint(joueurs)
# Test d'autres méthodes pour afficher la base de données des joueurs
pprint(ctrl.ctrl_manager.manager.db_players)
"""

"""
# Afficher la base de données des tournois
for tournament in ctrl.ctrl_manager.manager.db_tournois: 
    pprint(tournament)
"""
"""
# Test d'autres méthodes pour afficher la base de données des tournois
pprint(ctrl.ctrl_manager.manager.db_tournois)
"""