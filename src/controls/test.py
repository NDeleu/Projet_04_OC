"""
def other_round(self, tournoi_number, round_number):
    sorted_by_round_point = sorted(
        self.manager.list_all_tournoi[tournoi_number -1].player_list, key=lambda x: x.round_point, reverse=True)
    sorted_by_round_point_extend = sorted_by_round_point
    sorted_by_round_point_extend.append("Out")
    for y in range(int(len(sorted_by_round_point) / 2)):
        self.match_control.add_match(
            tournoi_number, round_number, y + 1,
            self.test_player1_matches_round(sorted_by_round_point_extend, tournoi_number, round_number),
            self.test_player2_matches_round(sorted_by_round_point_extend, tournoi_number, round_number))


# Vérifie si la liste match de ce round existe
def test_player1_matches_round(self, list_played, tournoi_number, round_number):
    if self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
        return self.test_player1_in_round(list_played, tournoi_number, round_number)
    else:
        return list_played[0]

# Vérifie si le joueur est déjà dans un match du round
def test_player1_in_round(self, list_played, tournoi_number, round_number):
    for player in list_played:
        if self.test_player_in_round_incept(player, tournoi_number, round_number) is False:
            pass
        else:
            return player

def test_player2_matches_round(self, list_played, tournoi_number, round_number):
    if self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
        return self.test_player2_in_round(list_played, tournoi_number, round_number)
    else:
        for player in list_played:
            if player == self.test_player1_matches_round(list_played, tournoi_number, round_number):
                pass
            elif player in self.test_player1_matches_round(list_played, tournoi_number, round_number).encountered:
                pass
            else:
                return player

def test_player2_in_round(self, list_played, tournoi_number, round_number):
    for player in list_played:
        if player == "Out":
            for players in list_played:
                if self.test_player_in_round_incept(players, tournoi_number, round_number) is False:
                    pass
                elif players == self.test_player1_matches_round(list_played, tournoi_number, round_number):
                    pass
                else:
                    return players
        elif self.test_player_in_round_incept(player, tournoi_number, round_number) is False:
            pass
        elif player == self.test_player1_matches_round(list_played, tournoi_number, round_number):
            pass
        elif player in self.test_player1_matches_round(list_played, tournoi_number, round_number).encountered:
            pass
        else:
            return player

def test_player_in_round_incept(self, player, tournoi_number, round_number):
    for matching in self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
        if player == matching.player1 or player == matching.player2:
            return False
"""
