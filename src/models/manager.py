from tinydb import TinyDB, Query


class Manager:
    def __init__(self):
        self.db = TinyDB("db.json")
        self.seek = Query()
        self.db_tournois = self.db.table("all_tournois")
        self.db_players = self.db.table("all_players")

