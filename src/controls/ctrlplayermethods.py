from src.models.playerdisplayed import PlayerDisplayed
from src.models.playerregistered import PlayerRegistered
from src.views.showplayer import ShowPlayer


class CtrlPlayerMethods:
    def __init__(self, view_main, manager_main):
        self.player_registered = PlayerRegistered
        self.player_displayed = PlayerDisplayed
        self.show_player = ShowPlayer()
        self.view_main = view_main
        self.manager_main = manager_main
        self.name_len_min = 3
        self.name_len_max = 15
        self.surname_len_min = 3
        self.surname_len_max = 15

    def init_dict_player_register(self):
        return {"name": self.name_player_register(),
                "surname": self.surname_player_register(),
                "id_chess": self.id_chess_player_register(),
                "total_points": 0,
                "birthday": self.birthday_player_register()}

    def name_player_register(self):
        print(self.show_player.init_name_player_register(self.name_len_min, self.name_len_max))
        return self.view_main.view_input.try_alphanum_string_input(self.name_len_min, self.name_len_max)

    def surname_player_register(self):
        print(self.show_player.init_surname_player_register(self.surname_len_min, self.surname_len_max))
        return self.view_main.view_input.try_alphanum_string_input(self.surname_len_min, self.surname_len_max)

    def id_chess_player_register(self):
        print(self.show_player.init_id_chess_player_register())
        answer = self.view_main.view_input.try_id_player_input()
        if self.view_main.view_input.try_already_exists(
                "identifiant joueur", answer, self.manager_main.check_main.check_models.check_player_exists(answer)):
            return answer
        else:
            return self.id_chess_player_register()

    def birthday_player_register(self):
        print(self.show_player.init_birthday_player_register())
        answer = self.view_main.view_input.try_date_input()
        return answer.strftime("%Y-%m-%d")

"""
class ControlPlayer:
    def __init__(self, manager):
        self.player = Player
        self.manager = manager

    def init_player(self, name, surname, naissance, identifiant):
        return self.player(name, surname, naissance, identifiant)

    def add_player(self, name, surname, naissance, identifiant):
        self.manager.list_all_player.append(self.init_player(name, surname, naissance, identifiant))
        self.manager.creat_player_to_json(len(self.manager.list_all_player))

    def load_player_by_idplayer(self, identifiant_player):
        self.manager.list_all_player.append(
            self.player(**self.manager.load_player_to_json_by_idplayer(identifiant_player)))

    def load_player_by_idjson(self, player_number):
        self.manager.list_all_player.append(
            self.player(**self.manager.load_player_to_json_by_idjson(player_number)))

    def load_all_player(self):
        for y in range(self.manager.len_list_player()):
            self.load_player_by_idjson(y+1)

    def calcul_total_point(self, players):
        for tournoi in self.manager.list_all_tournoi:
            for rounding in tournoi.round:
                for matching in rounding.match:
                    if players == matching.result_match[0][0]:
                        players.total_point += matching.result_match[0][1]
                    elif players == matching.result_match[1][0]:
                        players.total_point += matching.result_match[1][1]

    def init_total_point(self):
        for players in self.manager.list_all_player:
            players.total_point = 0
            self.calcul_total_point(players)
            self.manager.save_total_point_player_to_json(players)
"""

