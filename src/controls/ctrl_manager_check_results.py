
class CtrlManagerCheckResults:
    def __init__(self, manager):
        self.manager_to_check_results = manager

    def check_round_point_player(self, tournament_name, player_id):
        round_point_calculated = 0
        for matches in self.manager_to_check_results.db_matches.all():
            if matches["tournament_name"] == tournament_name:
                if matches["result_match"]:
                    if matches["result_match"][0][0]["id_chess"] == player_id:
                        round_point_calculated += float(
                            matches["result_match"][0][1])
                    elif matches["result_match"][1][0][
                            "id_chess"] == player_id:
                        round_point_calculated += float(
                            matches["result_match"][1][1])
                    else:
                        pass
                else:
                    pass
            else:
                pass
        return round_point_calculated

    def check_encountered_player(self, tournament_name, player_id):
        list_encountered = []
        for matches in self.manager_to_check_results.db_matches.all():
            if matches["tournament_name"] == tournament_name:
                if matches["result_match"]:
                    if matches["result_match"][0][0]["id_chess"] == player_id:
                        list_encountered.append(
                            matches["result_match"][1][0]["id_chess"])
                    elif matches["result_match"][1][0][
                            "id_chess"] == player_id:
                        list_encountered.append(
                            matches["result_match"][0][0]["id_chess"])
                    else:
                        pass
                else:
                    pass
            else:
                pass
        return list_encountered

    def check_total_point_player(self, player_id):
        total_point_calculated = 0
        for matches in self.manager_to_check_results.db_matches.all():
            if matches["result_match"]:
                if matches["result_match"][0][0]["id_chess"] == player_id:
                    total_point_calculated += float(matches[
                                                    "result_match"][0][1])
                elif matches["result_match"][1][0]["id_chess"] == player_id:
                    total_point_calculated += float(matches[
                                                    "result_match"][1][1])
                else:
                    pass
            else:
                pass
        return total_point_calculated
