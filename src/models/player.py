
class Player:
    def __init__(self, name, surname, naissance, identifiant):
        self.name = name
        self.surname = surname
        self.naissance = naissance
        self.identifiant = identifiant
        self.round_point = 0
        self.encountered = []
        self.total_point = 0

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return str(self)
