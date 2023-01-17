from tinydb import TinyDB, Query


class Manager:
    def __init__(self):
        self.db = TinyDB("db.json")
        self.seek = Query()
        self.db_players = self.db.table("all_players")
        self.db_tournaments = self.db.table("all_tournaments")
        self.db_rounds = self.db.table("all_rounds")
        self.db_matches = self.db.table("all_matches")
