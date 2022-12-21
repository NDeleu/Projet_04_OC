import datetime


class Round:
    def __init__(self, round_number, start_time):
        self.name = f"Round{round_number}"
        self.match = []
        self.start_time = start_time
        self.end_time = datetime

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)
