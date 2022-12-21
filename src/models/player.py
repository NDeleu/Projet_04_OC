
class Player:
    def __init__(self, name, surname, age, rank):
        self.name = name
        self.surname = surname
        self.age = age
        self.rank = rank
        self.round_point = 0
        self.encountered = []

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return str(self)
