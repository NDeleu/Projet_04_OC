
class CtrlManagerInsert:
    def __init__(self, manager):
        self.manager_to_insert = manager

    def insert_tournament_to_database(self, instance_tournament):
        self.manager_to_insert.db_tournaments.insert(instance_tournament)

    def insert_player_to_database(self, instance_player):
        self.manager_to_insert.db_players.insert(instance_player)

    def insert_rounds_to_database(self, instance_round):
        self.manager_to_insert.db_rounds.insert(instance_round)

    def insert_matches_to_database(self, instance_match):
        self.manager_to_insert.db_matches.insert(instance_match)

    def insert_players_to_tournament_to_database(self, tournament_name, list_players):
        self.manager_to_insert.db_tournaments.update({"player_list": list_players},
                                                     self.manager_to_insert.seek.name == tournament_name)

    def insert_rounds_to_tournament_to_database(self, tournament_name, list_rounds):
        self.manager_to_insert.db_tournaments.update({"rounds": list_rounds},
                                                     self.manager_to_insert.seek.name == tournament_name)

    def insert_date_to_tournament_to_database(self, tournament_name, list_date):
        self.manager_to_insert.db_tournaments.update({"date": list_date},
                                                     self.manager_to_insert.seek.name == tournament_name)

    def insert_matches_to_rounds_to_database(self, tournament_name, round_name, list_matches):
        self.manager_to_insert.db_rounds.update({"match": list_matches},
                                                (self.manager_to_insert.seek.tournament_name == tournament_name) &
                                                (self.manager_to_insert.seek.name == round_name))
