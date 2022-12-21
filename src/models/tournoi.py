from .round import Round


class Tournoi:
    def __init__(self, name, lieu, control_temps, tours_round=4):
        self.name = name
        self.lieu = lieu
        self.date = []
        self.tours_round = tours_round
        self.round = []
        self.player_list = []
        self.control_temps = control_temps
        self.description = str

    def __str__(self):
        return f"{self.name} à {self.lieu}"

    def __repr__(self):
        return str(self)


