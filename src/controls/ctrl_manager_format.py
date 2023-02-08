
class CtrlManagerFormat:
    def __init__(self, manager):
        self.manager_to_format = manager

    def player_register_to_displayed(dict_receive):
        dict_return = {"name": dict_receive["name"],
                       "surname": dict_receive["surname"],
                       "id_chess": dict_receive["id_chess"]}
        return dict_return

    player_register_to_displayed = staticmethod(player_register_to_displayed)

    def round_register_to_displayed(dict_receive):
        dict_return = {"name": dict_receive["name"],
                       "tournament_name": dict_receive["tournament_name"]}
        return dict_return

    round_register_to_displayed = staticmethod(round_register_to_displayed)

    def match_register_to_displayed(dict_receive):
        dict_return = {"name": dict_receive["name"],
                       "round_name": dict_receive["round_name"],
                       "tournament_name": dict_receive["tournament_name"]}
        return dict_return

    match_register_to_displayed = staticmethod(match_register_to_displayed)

    def format_update_players_to_tournament_to_database(list_player):
        list_return = []
        for player in list_player:
            list_return.append(player.__dict__)
        return list_return

    format_update_players_to_tournament_to_database = staticmethod(
        format_update_players_to_tournament_to_database)

    def format_update_rounds_to_tournament_to_database(list_rounds):
        list_return = []
        for rounds in list_rounds:
            list_return.append(rounds.__dict__)
        return list_return

    format_update_rounds_to_tournament_to_database = staticmethod(
        format_update_rounds_to_tournament_to_database)

    def format_data_results_all_players(list_dict_player):
        dict_return = {}
        for dict_player in list_dict_player:
            dict_return[
                f"player{list_dict_player.index(dict_player)}"] = dict_player
        return dict_return

    format_data_results_all_players = staticmethod(
        format_data_results_all_players)

    def format_data_results_all_tournaments(list_dict_tournament):
        dict_return = {}
        for dict_tournament in list_dict_tournament:
            dict_return[
                f"tournament{list_dict_tournament.index(dict_tournament)}"
            ] = dict_tournament
        return dict_return

    format_data_results_all_tournaments = staticmethod(
        format_data_results_all_tournaments)

    def format_data_results_player_list_tournament(self, list_dict_player):
        if not list_dict_player:
            return []
        else:
            list_return = self.init_format_data_results_player_list_tournament(
                list_dict_player)
            dict_return = {}
            for dict_player_tournament in list_return:
                dict_return[
                    f"player{list_return.index(dict_player_tournament)}"
                ] = dict_player_tournament
            return dict_return

    def init_format_data_results_player_list_tournament(list_dict_player):
        list_return = []
        for player_dict in list_dict_player:
            list_return.append({"name": player_dict["name"],
                                "surname": player_dict["surname"],
                                "id_chess": player_dict["id_chess"]})
        return list_return

    init_format_data_results_player_list_tournament = staticmethod(
        init_format_data_results_player_list_tournament)
