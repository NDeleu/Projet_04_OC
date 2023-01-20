from src.models.manager import Manager
from src.controls.ctrlmanagercheckmain import CtrlManagerCheckMain
from src.controls.ctrlmanagerupdate import CtrlManagerUpdate
from src.controls.ctrlmanagerinsert import CtrlManagerInsert
from src.controls.ctrlmanagerformat import CtrlManagerFormat


class CtrlManagerMain:
    def __init__(self):
        self.manager = Manager()
        self.check_main = CtrlManagerCheckMain(self.manager)
        self.manager_update = CtrlManagerUpdate(self.manager)
        self.manager_insert = CtrlManagerInsert(self.manager)
        self.manager_format = CtrlManagerFormat(self.manager)


"""
class ControlManager:
    def __init__(self):
        self.list_all_tournoi = []
        self.list_all_player = []
        self.manager = Manager()

    def save_total_point_player_to_json(self, player):
        self.manager.db_players.update(
            {"total_point": player.total_point},
            self.manager.seek.identifiant == player.identifiant)

    def load_player_to_json_by_idplayer(self, identifiant_player):
        return self.manager.db_players.search(self.manager.seek.identifiant == identifiant_player)[0]

    def load_player_to_json_by_idjson(self, player_number):
        return self.manager.db_players.get(doc_id=player_number)

    def clear_list_player(self):
        self.list_all_player.clear()

    def clear_list_tournoi(self):
        self.list_all_tournoi.clear()

    def len_list_player(self):
        return len(self.manager.db_players)

    def len_list_tournoi(self):
        return len(self.manager.db_tournois)

    def creat_tournoi_to_json(self, tournoi_number):
        self.manager.db_tournois.insert(self.dict_tournoi_to_json(tournoi_number))

    def save_date_tournoi_to_json(self, tournoi_number):
        self.manager.db_tournois.update(
            {"date": self.list_all_tournoi[tournoi_number-1].date},
            self.manager.seek.name == self.list_all_tournoi[tournoi_number-1].name)

    def save_round_tournoi_to_json(self, tournoi_number):
        self.manager.db_tournois.update(
            {"round": self.init_dict_rounds(tournoi_number)},
            self.manager.seek.name == self.list_all_tournoi[tournoi_number-1].name)

    def save_players_tournoi_to_json(self, tournoi_number):
        self.manager.db_tournois.update(
            {"player_list": self.init_dict_players(tournoi_number)},
            self.manager.seek.name == self.list_all_tournoi[tournoi_number-1].name)

    def save_description_tournoi_to_json(self, tournoi_number):
        self.manager.db_tournois.update(
            {"description": self.list_all_tournoi[tournoi_number-1].description},
            self.manager.seek.name == self.list_all_tournoi[tournoi_number-1].name)

    def load_tournoi_to_json_by_id(self, id_tournoi):
        return self.manager.db_tournois.get(doc_id=id_tournoi)

    def load_tournoi_to_json_by_name(self, name_tournoi):
        return self.manager.db_tournois.search(self.manager.seek.name == name_tournoi)[0]

    def dict_player_to_json(self, player_number):
        return {"name": self.list_all_player[player_number-1].name,
                "surname": self.list_all_player[player_number-1].surname,
                "naissance": self.list_all_player[player_number-1].naissance,
                "identifiant": self.list_all_player[player_number-1].identifiant,
                "total_point": self.list_all_player[player_number-1].total_point}

    def creat_player_to_json(self, player_number):
        self.manager.db_players.insert(self.dict_player_to_json(player_number))

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
        for matchs in rounds.match:
            list_init_matchs.append(self.dict_match_to_json(matchs))
        return list_init_matchs

    def init_dict_players(self, tournoi_number):
        list_init_players = []
        for players in self.list_all_tournoi[tournoi_number-1].player_list:
            list_init_players.append(self.dict_player_to_json(self.list_all_player.index(players)))
        return list_init_players

    def init_dict_result_match(self, match):
        result_match = ([self.dict_player_to_json(self.list_all_player.index(match.result_match[0][0])),
                         match.result_match[0][1]],
                        [self.dict_player_to_json(self.list_all_player.index(match.result_match[1][0])),
                         match.result_match[1][1]])
        return result_match

    def dict_match_to_json(self, match):
        return {"name": match.name,
                "player1": self.dict_player_to_json(self.list_all_player.index(match.player1)),
                "player2": self.dict_player_to_json(self.list_all_player.index(match.player2)),
                "result_match": self.init_dict_result_match(match)}

    def link_player_class(self, dict_to_class):
        for ply in self.list_all_player:
            if dict_to_class["identifiant"] == ply.identifiant:
            # if dict_to_class == self.dict_player_to_json(self.list_all_player.index(ply)):
                return ply
        return False
"""