
class CtrlManagerInsert:
    def __init__(self, manager):
        self.manager_to_insert = manager

    def insert_tournament_to_database(self, instance_tournament):
        self.manager_to_insert.db_tournaments.insert(instance_tournament)

    def insert_player_to_database(self, instance_player):
        self.manager_to_insert.db_players.insert(instance_player)
