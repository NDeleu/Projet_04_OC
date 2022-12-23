







"""
# Round :

def first_round(self):
    sorted_by_rank = sorted(self.player_list, key=lambda x: x.rank)
    for y in range(int(len(sorted_by_rank) / 2)):
        self.match.append(
            MatchControl(y + 1, sorted_by_rank[y], sorted_by_rank[y + (int(len(sorted_by_rank) / 2))]))
        

# Round : arrangement des autres Rounds
def other_round(self):
    self.init_round_point_players(players)
    sorted_by_point = sorted(player_list, key=lambda x: x.round_point)
    for y in range(int(len(sorted_by_point) / 2)):
        round1.match.append(Match(y + 1, sorted_by_point[y], sorted_by_point[y + 1]))

 
# les deux prochaines methodes de round point seront pr la class TournoiControl, et non pas pour
    # RoundControl. Il faudra aussi veiller à ne pas considérer les matchs du round en cours pr éviter
    # les probs si on load une game ac un round en cours, à réfléchir...
def init_round_point_players(self):
    for player in self.player_list:
        self.round_point_player(player)

def round_point_player(self, player):
    player.round_point = 0
    # for matchs in rounds:
    for matching in self.match:
        if matching.result_match:
            if player == matching.result_match[0][0]:
                player.round_point += matching.result_match[0][1]
            elif player == matching.result_match[1][0]:
                player.round_point += matching.result_match[1][1]

def init_encountered_player(self):
    for player in self.player_list:
        self.encountered_player(player)

def encountered_player(self, player):
    player.encountered.clear()
    # for matchs in rounds:
    for matching in self.match:
        if matching.result_match:
            if player == matching.result_match[0][0]:
                player.encountered.append(matching.result_match[1][0])
            elif player == matching.result_match[1][0]:
                player.encountered.append(matching.result_match[0][0])

# Round : initialise les instances de matchs dans round.match et print les matchs en question demandant un résultat
def init_round(self):
    self.first_round()
    
# Round : print les matchs restants demandant un résultat
def show_match_to_record(self):
    for matching in self.match:
        if not matching.result_match:
            print(matching)

# Round : Conditionne l'emploi des fonctions init et show en fonction du fait qu'init est déjà eu lieu ou non
def test_round(self):
    if not self.match:
        self.init_round()
        self.show_match_to_record()
    else:
        self.show_match_to_record()
"""
