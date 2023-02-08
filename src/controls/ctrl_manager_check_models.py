
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

    def open_list_all_tournament_dict(self):
        list_dict = []
        for tournament in self.manager_to_check_models.db_tournaments.all():
            tournament_dict = {"date": tournament["date"],
                               "location": tournament["location"],
                               "name": tournament["name"]
                               }
            list_dict.append(tournament_dict)
            return list_dict

    def open_tournament_description(self, tournament_name):
        for tournament in self.manager_to_check_models.db_tournaments.all():
            if tournament["name"] == tournament_name:
                return {"name": tournament["name"],
                        "location": tournament["location"],
                        "time_control": tournament["time_control"],
                        "number_round": tournament["number_round"],
                        "date": tournament["date"],
                        "description": tournament["description"]}
            else:
                pass

    def open_tournament_player_list(self, tournament_name):
        for tournament in self.manager_to_check_models.db_tournaments.all():
            if tournament["name"] == tournament_name:
                return tournament["player_list"]
            else:
                return []

    def open_tournament_round_list(self, tournament_name):
        list_rounds = []
        for rounds in self.manager_to_check_models.db_rounds.all():
            if rounds["tournament_name"] == tournament_name:
                list_rounds.append(rounds["name"])
            else:
                pass
        return list_rounds

    def open_tournament_round_match_list(self, tournament_name):
        dict_return = {}
        list_rounds = self.open_tournament_round_list(tournament_name)
        for rounds in list_rounds:
            list_match_round = []
            for match in self.manager_to_check_models.db_matches.all():
                if match["tournament_name"] == tournament_name:
                    if match["round_name"] == rounds:
                        if match["result_match"]:
                            list_match_round.append(
                                (["{player1name} {player1surname}".format(
                                    player1name=match["result_match"][0][0][
                                        "name"],
                                    player1surname=match[
                                        "result_match"][0][0]["surname"]),
                                    match["result_match"][0][1]],
                                 ["{player2name} {player2surname}".format(
                                     player2name=match["result_match"][1][0][
                                         "name"],
                                     player2surname=match[
                                         "result_match"][1][0]["surname"]),
                                     match["result_match"][1][1]]))
                        else:
                            list_match_round.append(
                                "{player1name} {player1surname} vs "
                                "{player2name} {player2surname} : "
                                "résultats en attente".format(
                                    player1name=match["player1"][0],
                                    player1surname=match["player1"][1],
                                    player2name=match["player2"][0],
                                    player2surname=match["player2"[1]]))
                    else:
                        pass
                else:
                    pass
            dict_return[f"{rounds}"] = list_match_round
        return dict_return
