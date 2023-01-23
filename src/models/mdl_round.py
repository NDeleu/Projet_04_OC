
class Round:
    def __init__(self, name, tournament_name, match=None):
        if isinstance(name, int) or isinstance(name, float):
            self.name = f"Round{name}"
        else:
            if name.isdecimal():
                self.name = f"Round{name}"
            else:
                self.name = name
        self.tournament_name = tournament_name
        if match is None:
            self.match = []
        else:
            self.match = match
