

# round :

"""
pr le self.name, il est attendu Round1, Round2, Round3 etc
pourrai être défini par un "Round{}".format(tour_number)
implémenté ds la boucle for qui les appel

exemple test :
round1 = Round(["Jean"], 2)

print(round1)
tour_number = 1
round1.name = "Round{}".format(tour_number)
print(round1)
"""

"""
Pour le self.start_time : round1 = Round(["Jack"], 4, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
soit à initier au moment de la création de l'instance de round durant le running

Pour le self.end_time : round1.end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
soit à créer à la fin de l'action de round quand tous les match enregistrés et les résultats envoyés au modèle par 
le controleur, on en profite pr créer le self.end_time
"""

"""
pr round/match même principe que tournoi/round
pr self.name pour Match, principe plus ou moins similaire à self.name de Round
pr self.result pour Match, un tuple ac dedans 2 listes, => 
    ([joueur1, scorej1], [joueur2, scorej2])
    Ces scores peuvent être incrémentés à la fin du round ? mais où ?
        de pref, dans une liste où il y a les joueurs et leur score total, mais relatif au tournoi
            pr ne pas impacter les autres tournois quand il y a le mm joueur
            
exemple d'entrée dans match :
match1 = Match(["Jacques", "Micheline"])
match1.name = "match 1"

print(match1)

match1.result = (["Jacques", 1], ["Micheline", 0])

print(match1)
"""
