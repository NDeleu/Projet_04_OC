from .round import Round

class Tournoi:
    def __init__(self, name, tours_round=4):
        self.name = name
        self.liste_joueur = []
        self.tours_round = tours_round
        self.round = Round(self.liste_joueur, self.tours_round)

    def join_players(self, liste_joueur):
        for player in liste_joueur :
            self.liste_joueur.append(player)