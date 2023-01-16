
class Round:
    def __init__(self):
        pass


"""
class Round:
    def __init__(self, name, start_time, match=None, end_time=None):
        if isinstance(name, int) or isinstance(name, float):
            self.name = f"Round{name}"
        else:
            if name.isdecimal():
                self.name = f"Round{name}"
            else:
                self.name = name
        if match is None:
            self.match = []
        else:
            self.match = match
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)
"""