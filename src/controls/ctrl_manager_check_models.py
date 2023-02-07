
class CtrlManagerCheckModels:
    def __init__(self, manager):
        self.manager_to_check_models = manager

    def check_tournament_exists(self, tournament_name):
        for tournament in self.manager_to_check_models.db_tournaments.all():
            if tournament["name"] == tournament_name:
                return True
            else:
                pass
        return False

    def check_player_exists(self, id_player):
        for player in self.manager_to_check_models.db_players.all():
            if player["id_chess"] == id_player:
                return True
            else:
                pass
        return False

    def open_load_tournament(self, tournament_name):
        for tournament in self.manager_to_check_models.db_tournaments.all():
            if tournament["name"] == tournament_name:
                return tournament
            else:
                pass
        return None

    def open_load_player(self, id_player):
        for player in self.manager_to_check_models.db_players.all():
            if player["id_chess"] == id_player:
                return player
            else:
                pass
        return None

    def open_load_rounds(self, name, tournament_name):
        for rounds in self.manager_to_check_models.db_rounds.all():
            if rounds["tournament_name"] == tournament_name:
                if rounds["name"] == name:
                    return rounds
                else:
                    pass
            else:
                pass
        return None

    def open_load_matches(self, name, round_name, tournament_name):
        for matches in self.manager_to_check_models.db_matches.all():
            if matches["tournament_name"] == tournament_name:
                if matches["round_name"] == round_name:
                    if matches["name"] == name:
                        return matches
                    else:
                        pass
                else:
                    pass
            else:
                pass
        return None

    def open_load_all_matches_from_tournament(self, tournament_name):
        list_match = []
        for matches in self.manager_to_check_models.db_matches.all():
            if matches["tournament_name"] == tournament_name:
                list_match.append(matches)
            else:
                pass
        return list_match

    def return_date_start_round(self, name, tournament_name):
        for rounds in self.manager_to_check_models.db_rounds.all():
            if rounds["tournament_name"] == tournament_name:
                if rounds["name"] == name:
                    return rounds["start_time"]
                else:
                    pass
            else:
                pass
        return None

    def return_date_end_round(self, name, tournament_name):
        for rounds in self.manager_to_check_models.db_rounds.all():
            if rounds["tournament_name"] == tournament_name:
                if rounds["name"] == name:
                    return rounds["end_time"]
                else:
                    pass
            else:
                pass
        return None

    def check_end_time_rounds_exists(self, name, tournament_name):
        for rounds in self.manager_to_check_models.db_rounds.all():
            if rounds["tournament_name"] == tournament_name:
                if rounds["name"] == name:
                    if rounds["end_time"] != "Le Round n'est " \
                                             "pas encore terminé":
                        return True
                    else:
                        pass
                else:
                    pass
            else:
                pass
        return False

    def open_list_all_player_dict(self):
        list_dict = []
        for player in self.manager_to_check_models.db_players.all():
            list_dict.append(player)
        return list_dict
