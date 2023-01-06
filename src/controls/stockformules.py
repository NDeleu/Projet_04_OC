from tinydb import TinyDB, Query, where
from pprint import pprint

# Tournoi :
# view :
"""
Créer ds le view une condition au contrôle du tps : soit :
    Bullet
    Blitz
    Coup Rapide
un des 3 pas autre chose
"""
"""
proposer input de description, exemple d'utilisation : tournoi1.description = "Yo je suis le président"
"""
"""
db = TinyDB("db.json")


class Tournoi:
    def __init__(self, name, rounds=None, joueurs=None):
        self.name = name
        if rounds is None:
            self.rounds = []
        else:
            self.rounds = rounds
        if joueurs is None:
            self.joueurs = []
        else:
            self.joueurs = joueurs

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def init_dict_rounds(self):
        list_init_round = []
        for rounds in self.rounds:
            list_init_round.append(rounds.dict_round_to_json())
        return list_init_round

    def init_dict_players(self):
        list_init_players = []
        for players in self.joueurs:
            list_init_players.append(players.__dict__)
        return list_init_players

    def dict_tournoi_to_json(self):
        return {"name": self.name, "rounds": self.init_dict_rounds(), "joueurs": self.init_dict_players()}


class Round:
    def __init__(self, name, match=None):
        self.name = name
        if match is None:
            self.match = []
        else:
            self.match = match

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def init_dict_matchs(self):
        list_init_matchs = []
        for matchs in self.match:
            list_init_matchs.append(matchs.__dict__)
        return list_init_matchs

    def dict_round_to_json(self):
        return {"name": self.name, "match": self.init_dict_matchs()}

class Match:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Player:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


databasetournoi = db.table("totaltournois")
databasejoueurs = db.table("totaljoueurs")
"""
"""
pl1 = Player("Rond", "Jean", 18)
pl2 = Player("Carre", "Patrick", 21)
pl3 = Player("Reactangle", "Fabrice", 15)
pl4 = Player("Losange", "Marc", 26)

tournoi1 = Tournoi("t1")
tournoi2 = Tournoi("t2")

tournoi1.rounds.append(Round("r1"))
tournoi1.rounds.append(Round("r2"))

tournoi2.rounds.append(Round("r1"))
tournoi2.rounds.append(Round("r2"))

tournoi1.rounds[0].match.append(Match("m1"))
tournoi1.rounds[0].match.append(Match("m2"))
tournoi1.rounds[1].match.append(Match("m1"))
tournoi1.rounds[1].match.append(Match("m2"))

tournoi2.rounds[0].match.append(Match("m1"))
tournoi2.rounds[0].match.append(Match("m2"))
tournoi2.rounds[1].match.append(Match("m1"))
tournoi2.rounds[1].match.append(Match("m2"))

tournoi1.joueurs.append(pl1)
tournoi1.joueurs.append(pl2)
tournoi1.joueurs.append(pl3)
tournoi1.joueurs.append(pl4)

tournoi2.joueurs.append(pl1)
tournoi2.joueurs.append(pl2)
tournoi2.joueurs.append(pl3)
tournoi2.joueurs.append(pl4)

databasejoueurs.insert(pl1.__dict__)
databasejoueurs.insert(pl2.__dict__)
databasejoueurs.insert(pl3.__dict__)
databasejoueurs.insert(pl4.__dict__)

databasetournoi.insert(tournoi1.dict_tournoi_to_json())
databasetournoi.insert(tournoi2.dict_tournoi_to_json())

pprint(databasetournoi.all())
pprint(databasejoueurs.all())
"""


# pprint(parties.all())

"""
def enter_list(liste_donnee):
    enter = []
    for l in liste_donnee:
        enter.append(l.__dict__)
    return enter


# pprint(parties.get(doc_id=1)["joueurs"][0])
"""



"""
Dans ctrl manager : 
    Player : Ajouter(append)
    Tournoi : Ajouter(append)
    Round : Ajouter(append)
    Match : Ajouter(append)/Modifier(replace)
"""

"""
pl3 = TestFor(**dict_test["players"][0])
print(pl3.__dict__)
print(pl3)
"""

"""
Donc check quand utiliser cette technique de désérialisation pr aller du json à l'instance de classe
"""
"""
tournoi1 = Tournoi(**databasetournoi.get(doc_id=1))

for y in range(len(tournoi1.rounds)):
    tournoi1.rounds[y] = Round(**tournoi1.rounds[y])
    for i in range(len(tournoi1.rounds[y].match)):
        tournoi1.rounds[y].match[i] = Match(**tournoi1.rounds[y].match[i])
"""
list_test = [1, 2, 3, 4]

list_test.append(5)

print(list_test[len(list_test)-1])