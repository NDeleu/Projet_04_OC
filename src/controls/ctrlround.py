"""
!!!
* Fusionner les roundspoint et les encounterplayer ds Round
* Ajouter date de fin à la fin de test_round(?) si autant de match que ceux prévu (list joueur/2)
* Envoyer nombre ds match à partir de round (qd record ds liste) + considérer fin match qd result_match ok
* Finir Other_Round en utilisant ranked round_point+not in list (créer une liste pr la méthode
    des noms déjà enregistrés) + not in encounter et faire une méthodception pr éviter le while
* Mettre les roundpts et encounter player dans la class ctrltournoi + technique pr éviter de refr dès le début
    en cas de reprise en plein round
* Utiliser la date de fin d'un Round pr passer au suivant dans la class ctrltournoi
* Envoyer nombre ds round à partir de tournoi (qd record ds liste)
* Record les dates des Rounds dans la liste des dates de Tournoi
* Réarranger tous les for pour [for...]
* mettre choix tours round ds tournoi
* mettre choix control temps ds tournoi
* proposer description ds tournoi
* changer résultats method pr match
* method pr add players ds player list ds tournoi
* trnamsttre liste joueur de tournoi à round
!!!
"""


"""
# Round : arrangement des autres Rounds
def other_round(players):
    init_round_point_players(players)
    sorted_by_point = sorted(player_list, key=lambda x: x.round_point)
    for y in range(int(len(sorted_by_point) / 2)):
        round1.match.append(Match(y+1, sorted_by_point[y], sorted_by_point[y+1]))


def init_round_point_players(players):
    for player in players:
        round_point_player(player)


def round_point_player(player):
    player.round_point = 0
    for matchs in rounds:
        for matching in matchs:
            if matching[0] == player:
                player.round_point += matching[1]
"""

"""
Lancer un nouveau round + vérifier et créer le nom du nouveau round + l'ajouter à la liste tournoi.round
!!!
a rework pour ne pas devoir utiliser un compter check round, mais en considérant la liste préalablement établie
ds tournoi (tournoi.round) : exemple : round{}.format(len(self.tournoi)      ???
Ou check directement ac le nom du précédent round ???
!!!

def round_start(self):
    if "round{}".format(self.check_round) not in self.round_match:
        self.round_match["round{}".format(self.check_round)] = []
        if "round{}".format(self.check_round) == "round1":
            self.first_round()
        else:
            self.other_round()
    else:
        if self.check_match < int(len(self.liste_joueur) / 2):
            print(
                "Vous n'avez pas fini le round en cours, veuillez saisir le résultat de tous les matchs du round en cours")
        else:
            self.check_round += 1
            self.check_match = 0
            self.round_start()
"""


"""
Lancer les matchs du premier round (ac ses règles spécifiques)
!!!
Parait bon, à recheck => changer la forme du for ac [for ... i in ...]
!!!

def first_round(self):
    sorted_by_classement = sorted(self.liste_joueur, key=lambda x: x.classement)
    for y in range(int(len(sorted_by_classement) / 2)):
        self.round_match["round{}".format(self.check_round)].append(
            (sorted_by_classement[y], sorted_by_classement[y + (int(len(sorted_by_classement) / 2))]))
"""


"""
Lancer les matchs des autres rounds (ac ses règles spécifiques)
!!!
L'idée est correct, mais préférer for à while, maybe implanter un système de pts aux joueurs, ou recalculer en fonction
des pts dans matchs (si pas trop long !), enfin fr passer la boucle for à [for ... i in ...]
!!!

def other_round(self):
    y = 0
    i = 1
    sorted_by_roundpoint = sorted(self.liste_joueur, key=lambda x: x.round_point)  # self.resultat joueur ?
    while int(len(self.round_match["round{}".format(self.check_round)]) < int(len(self.liste_joueur) / 2)):
        if (sorted_by_roundpoint[y], sorted_by_roundpoint[y + 1]) or (
                sorted_by_roundpoint[y + 1], sorted_by_roundpoint[y]) not in self.round_match:
            self.round_match["round{}".format(self.check_round)].append(
                (sorted_by_roundpoint[y], sorted_by_roundpoint[y + i]))
            del (sorted_by_roundpoint[y + i])
            del (sorted_by_roundpoint[y])
            i = 1
        else:
            i += 1
"""

