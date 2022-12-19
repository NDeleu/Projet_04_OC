class Round:
    def __init__(self):

        self.check_round = 1
        self.check_match = 0

    def initialisation_resultat_joueur(self):
        for player in self.liste_joueur:
            self.resultat_joueur[player] = []


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


    def first_round(self):
        sorted_by_classement = sorted(self.liste_joueur, key=lambda x: x.classement)
        for y in range(int(len(sorted_by_classement) / 2)):
            self.round_match["round{}".format(self.check_round)].append(
                (sorted_by_classement[y], sorted_by_classement[y + (int(len(sorted_by_classement) / 2))]))


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


    def match(self, match_number, score_joueur1, score_joueur2):
        self.check_match += 1
        if score_joueur1 == 1 and score_joueur2 == 0:
            self.resultat_joueur[self.round_match["round{}".format(self.check_round)][match_number][0]].append(1)
            self.resultat_joueur[self.round_match["round{}".format(self.check_round)][match_number][1]].append(0)

        elif score_joueur1 == 0 and score_joueur2 == 1:
            self.resultat_joueur[self.round_match["round{}".format(self.check_round)][match_number][0]].append(0)
            self.resultat_joueur[self.round_match["round{}".format(self.check_round)][match_number][1]].append(1)

        elif score_joueur1 == 0 and score_joueur2 == 0:
            self.resultat_joueur[self.round_match["round{}".format(self.check_round)][match_number][0]].append(0.5)
            self.resultat_joueur[self.round_match["round{}".format(self.check_round)][match_number][1]].append(0.5)

        else:
            print("erreur de saisie, veuillez réitérez, voir help()")


    def rematch(self, round_number, match_number, score_joueur1, score_joueur2):
        if score_joueur1 == 1 and score_joueur2 == 0:
            self.resultat_joueur[self.round_match["round{}".format(round_number)][match_number][0]][round_number - 1] = 1
            self.resultat_joueur[self.round_match["round{}".format(round_number)][match_number][1]][round_number - 1] = 0

        elif score_joueur1 == 0 and score_joueur2 == 1:
            self.resultat_joueur[self.round_match["round{}".format(round_number)][match_number][0]][round_number - 1] = 0
            self.resultat_joueur[self.round_match["round{}".format(round_number)][match_number][1]][round_number - 1] = 1

        elif score_joueur1 == 0 and score_joueur2 == 0:
            self.resultat_joueur[self.round_match["round{}".format(round_number)][match_number][0]][round_number - 1] = 0.5
            self.resultat_joueur[self.round_match["round{}".format(round_number)][match_number][1]][round_number - 1] = 0.5

        else:
            print("erreur de saisie, veuillez réitérez, voir help()")