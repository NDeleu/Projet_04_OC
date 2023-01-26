
class CtrlManagerFormat:
    def __init__(self, manager):
        self.manager_to_format = manager

    def player_register_to_displayed(dict_receive):
        dict_return = {"name": dict_receive["name"], "surname": dict_receive["surname"],
                       "id_chess": dict_receive["id_chess"]}
        return dict_return

    player_register_to_displayed = staticmethod(player_register_to_displayed)

    def round_register_to_displayed(dict_receive):
        dict_return = {"name": dict_receive["name"], "tournament_name": dict_receive["tournament_name"]}
        return dict_return

    round_register_to_displayed = staticmethod(round_register_to_displayed)

    def match_register_to_displayed(dict_receive):
        dict_return = {"name": dict_receive["name"],
                       "round_name": ["round_name"], "tournament_name": ["tournament_name"]}
        return dict_return

    match_register_to_displayed = staticmethod(match_register_to_displayed)

    def format_update_players_to_tournament_to_database(list_player):
        list_return = []
        for player in list_player:
            list_return.append(player.__dict__)
        return list_return

    format_update_players_to_tournament_to_database = staticmethod(format_update_players_to_tournament_to_database)
