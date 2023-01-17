
class Player:
    def __init__(self, name, surname, id_chess):
        self.name = name
        self.surname = surname
        self.id_chess = id_chess


"""
class Player:
    def __init__(self, name, surname, naissance, identifiant, round_point=0, encountered=None, total_point=0):
        self.name = name
        self.surname = surname
        self.naissance = naissance
        self.identifiant = identifiant
        self.round_point = round_point
        if encountered is None:
            self.encountered = []
        else:
            self.encountered = encountered
        self.total_point = total_point

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return str(self)
"""