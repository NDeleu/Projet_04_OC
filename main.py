from src.controls import MainControls
from src.models import Player
from src.models import Tournoi

"""
Création des instances de joueurs
"""
player1 = Player("Jean", "Duchemin", 35, 3)
player2 = Player("Marc", "Longdubas", 25, 2)
player3 = Player("Marcel", "Proust", 50, 4)
player4 = Player("Olivier", "Dupont", 32, 1)
player5 = Player("Lilian", "Hach", 40, 5)
player6 = Player("Fabrice", "Coler", 41, 7)
player7 = Player("Nicolas", "Jarva", 62, 6)
player8 = Player("Marc", "Dubois", 26, 8)

"""
Création de la liste des instances de joueurs
"""
test_liste = [player1, player2, player3, player4, player5, player6, player7, player8]


"""
Création de l'instance du tournoi
"""
tournoi1 = Tournoi("Le grand tournoi")


"""
Incorporation de la liste des instances joueurs dans l'instance tournoi
Incorporation de la liste des instances joueurs dans l'instance round
"""
tournoi1.join_players(test_liste)
tournoi1.round.initialisation_resultat_joueur()

"""
Liste des joueurs du tournoi
"""
# print(tournoi1.liste_joueur)

"""
Test recherche information à partir de cette liste, ici l'age du premier joueur
"""
# print(tournoi1.liste_joueur[0].age)

"""
Test de la liste vide des résultats des joueurs
"""
# print(tournoi1.round.resultat_joueur)


"""
Execution d'un round (premier)
"""
tournoi1.round.round_start()
# print(tournoi1.round.round_match)

"""
Execution d'un second round sans avoir saisie tous les résultats
"""
#tournoi1.round.round_start()
#print(tournoi1.round.round_match)

"""
Saisie des résultats du premier round
"""
tournoi1.round.match(0, 1, 0)
tournoi1.round.match(1, 0, 0)
tournoi1.round.match(2, 0, 1)
tournoi1.round.match(3, 1, 0)

"""
Execution d'un round (second)
"""
tournoi1.round.round_start()
# print(tournoi1.round.round_match)

"""
Visualisation des résultats des joueurs
"""
# print(tournoi1.round.resultat_joueur)

"""
Modification des résultats
"""
tournoi1.round.rematch(1, 0, 0, 1)

"""
Nouvelle visualiusation des résultats des joueurs après modification
"""
# print(tournoi1.round.resultat_joueur)



