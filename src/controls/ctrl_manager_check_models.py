import copy


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

