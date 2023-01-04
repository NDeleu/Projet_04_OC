
class Player:
    def __init__(self, name, surname, naissance, identifiant, rank):
        self.name = name
        self.surname = surname
        self.naissance = naissance
        self.identifiant = identifiant
        self.rank = rank
        self.round_point = 0
        self.encountered = []

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return str(self)
