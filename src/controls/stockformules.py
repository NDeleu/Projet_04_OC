

# Tournoi :
"""
def join_players(self, liste_joueur):
    for player in liste_joueur:
        self.liste_joueur.append(player)

!!! Il faut une liste des indices correspondant aux instances de joueurs stockés ds tinydb !!!
"""
"""
Créer la même pour self.date et self.round

indice pr round : Round(self.liste_joueur, self.tours_round)

Pour la date, aller chercher les dates de round, mais en changeant le format, soit :
print(datetime.datetime.strptime(round1.start_time, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"))
pour cela on va repasser la date de str à objet, puis de objet en str en lui demandant de ne prendre que année mois jour
puis on fait un self.date.append(la date qu'on a créé) avec condition qu'il n'existe pas, donc :
if not datecréé in self.date :
    self.date.append(datecréé) 
"""

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
