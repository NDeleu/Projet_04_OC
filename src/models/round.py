import datetime


class Round:
    def __init__(self, round_number, start_time, match=None, end_time=None):
        if isinstance(round_number, int) or isinstance(round_number, float):
            self.name = f"Round{round_number}"
        else:
            if round_number.isdecimal():
                self.name = f"Round{round_number}"
            else:
                self.name = round_number
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
