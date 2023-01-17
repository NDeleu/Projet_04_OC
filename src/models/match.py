
class Match:
    def __init__(self, name, round_name, tournament_name):
        if isinstance(name, int) or isinstance(name, float):
            self.name = f"Match{name}"
        else:
            if name.isdecimal():
                self.name = f"Match{name}"
            else:
                self.name = name
        self.round_name = round_name
        self.tournament_name = tournament_name
