"""
from tinydb import TinyDB

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age


player = Player(name='John', age=22)

serialized_player = {
    'name': player.name,
    'age': player.age
}


serialized_players = [serialized_player]

db = TinyDB("db.json")
players_table = db.table("players")
players_table.truncate()
players_table.insert_multiple(serialized_players)

serialized_players = players_table.all()

name = serialized_player["name"]
age = serialized_player["age"]
player = Player(name=name, age=age)

print(serialized_players)
"""


