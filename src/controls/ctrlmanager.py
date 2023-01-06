from src.models import Manager


class ControlManager:
    def __init__(self):
        self.list_all_tournoi = []
        self.list_all_player = []
        self.manager = Manager()

    def creat_player_to_json(self, player_number):
        self.manager.db_players.insert(self.dict_player_to_json(player_number))

    def save_player_to_json(self, player_number):
        self.manager.db_players.update(self.dict_player_to_json(player_number))

    def load_player_to_json(self, player_number):
        return self.manager.db_players.get(doc_id=player_number)

    def creat_tournoi_to_json(self, tournoi_number):
        self.manager.db_tournois.insert(self.dict_tournoi_to_json(tournoi_number))

    def save_tournoi_to_json(self, tournoi_number):
        self.manager.db_tournois.update(self.dict_tournoi_to_json(tournoi_number))

    def load_tournoi_to_json(self):
        pass

    def dict_player_to_json(self, player_number):
        return {"name": self.list_all_player[player_number-1].name,
                "surname": self.list_all_player[player_number-1].surname,
                "naissance": self.list_all_player[player_number-1].naissance,
                "identifiant": self.list_all_player[player_number-1].identifiant,
                "total_point": self.list_all_player[player_number-1].total_point}

    def dict_tournoi_to_json(self, tournoi_number):
        return {"name": self.list_all_tournoi[tournoi_number-1].name,
                "lieu": self.list_all_tournoi[tournoi_number-1].lieu,
                "date": self.list_all_tournoi[tournoi_number-1].date,
                "tours_round": self.list_all_tournoi[tournoi_number-1].tours_round,
                "round": self.init_dict_rounds(tournoi_number),
                "player_list": self.init_dict_players(tournoi_number),
                "control_temps": self.list_all_tournoi[tournoi_number-1].control_temps,
                "description": self.list_all_tournoi[tournoi_number-1].description}

    def init_dict_rounds(self, tournoi_number):
        list_init_round = []
        for rounds in self.list_all_tournoi[tournoi_number-1].round:
            list_init_round.append(self.dict_round_to_json(rounds))
        return list_init_round

    def dict_round_to_json(self, rounds):
        return {"name": rounds.name,
                "match": self.init_dict_matchs(rounds),
                "start_time": rounds.start_time,
                "end_time": rounds.end_time}

    def init_dict_matchs(self, rounds):
        list_init_matchs = []
        for matchs in rounds:
            list_init_matchs.append(self.dict_match_to_json(matchs))
        return list_init_matchs

    def init_dict_players(self, tournoi_number):
        list_init_players = []
        for players in self.list_all_tournoi[tournoi_number-1].player_list:
            list_init_players.append(self.dict_player_to_json(
                self.manager.db_players.search(
                    self.manager.seek.identifiant == players.identifiant)))
        return list_init_players

    def init_dict_result_match(self, match):
        result_match = ([self.dict_player_to_json((
            self.manager.db_players.get(
                self.manager.seek.identifiant == match.result_match[0][0].identifiant).doc_id)),
                            match.result_match[0][1]], [
            self.dict_player_to_json((
                self.manager.db_players.get(
                    self.manager.seek.identifiant == match.result_match[1][0].identifiant).doc_id)),
            match.result_match[1][1]])
        return result_match

    def dict_match_to_json(self, match):
        return {"name": match.name,
                "player1": self.dict_player_to_json((
                    self.manager.db_players.get(
                        self.manager.seek.identifiant == match.player1.identifiant).doc_id)),
                "player2": self.dict_player_to_json((
                    self.manager.db_players.get(
                        self.manager.seek.identifiant == match.player2.identifiant).doc_id)),
                "result_match": self.init_dict_result_match(match)}
