from src.models import Match


class ControlMatch:
    def __init__(self, manager):
        self.match = Match
        self.manager = manager

    def init_match(self, match_number, player1, player2):
        return self.match(match_number, player1, player2)

    def add_match(self, tournoi_number, round_number, match_number, player1, player2):
        self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match.append(self.init_match(
            match_number, player1, player2))

    # input result match

    def input_result_match(self, tournoi_number, round_number, match_number, result_player1, result_player2):
        self.match.result_match = (
            [self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match[match_number-1].player1,
             result_player1],
            [self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match[match_number-1].player2,
             result_player2])
        return self.match.result_match

    def add_result_match(self, tournoi_number, round_number, match_number, result_player1, result_player2):
        self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match[match_number-1] = \
            self.input_result_match(tournoi_number, round_number, match_number, result_player1, result_player2)