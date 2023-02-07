

class Tournament:
    def __init__(
            self, name, location, time_control,
            number_round=4, player_list=None,
            rounds=None, date=None, description=None):
        self.name = name
        self.location = location
        if date is None:
            self.date = []
        else:
            self.date = date
        self.number_round = number_round
        if rounds is None:
            self.rounds = []
        else:
            self.rounds = rounds
        if player_list is None:
            self.player_list = []
        else:
            self.player_list = player_list
        self.time_control = time_control
        if description is None:
            self.description = "Aucune description"
        else:
            self.description = description

    def __str__(self):
        return f"{self.name} à {self.location}"

    def __repr__(self):
        return str(self)
