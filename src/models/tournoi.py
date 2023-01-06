from .round import Round


class Tournoi:
    def __init__(self, name, lieu, control_temps, tours_round=4, player_list=None, rounds=None,
                 date=None, description=None):
        self.name = name
        self.lieu = lieu
        if date is None:
            self.date = []
        else:
            self.date = date
        self.tours_round = tours_round
        if rounds is None:
            self.round = []
        else:
            self.round = rounds
        if player_list is None:
            self.player_list = []
        else:
            self.player_list = player_list
        self.control_temps = control_temps
        if description is None:
            self.description = str
        else:
            self.description = description

    def __str__(self):
        return f"{self.name} à {self.lieu}"

    def __repr__(self):
        return str(self)


