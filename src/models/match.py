

class Match:
    def __init__(self, match_number, player1, player2, result_match=None):
        if isinstance(match_number, int) or isinstance(match_number, float):
            self.name = f"Match{match_number}"
        else:
            if match_number.isdecimal():
                self.name = f"Match{match_number}"
            else:
                self.name = match_number
        self.player1 = player1
        self.player2 = player2
        if result_match is None:
            self.result_match = ()
        else:
            self.result_match = result_match

    def __str__(self):
        if not self.result_match:
            return f"{self.name} : {self.player1} vs {self.player2}"

        else:
            return f"{self.name} : {self.result_match}"

    def __repr__(self):
        return str(self)
