from src.models.mdl_round_displayed import RoundDisplayed
from src.models.mdl_round_registered import RoundRegistered
from src.views.view_show_round import ShowRound
import datetime


class CtrlRoundMethods:
    def __init__(self, manager_main):
        self.round_registered = RoundRegistered
        self.round_displayed = RoundDisplayed
        self.show_round = ShowRound()
        self.manager_main = manager_main

    def init_dict_round_register(name, tournament_name):
        return {"name": name,
                "tournament_name": tournament_name,
                "start_time": datetime.datetime.now().strftime("%Y-%m-%d")}

    init_dict_round_register = staticmethod(init_dict_round_register)

    def init_create_round_registered(self, name, tournament_name):
        dict_to_record = self.init_dict_round_register(name, tournament_name)
        return self.round_registered(**dict_to_record)

    def register_round(self, name, tournament_name):
        round_instance = self.init_create_round_registered(name, tournament_name)
        self.manager_main.manager_insert.insert_rounds_to_database(round_instance.__dict__)

    def load_round_to_tournament(self, name, tournament_name):
        return self.round_displayed(**
                                    self.manager_main.manager_format.round_register_to_displayed(
                                        self.manager_main.check_main.check_models.open_load_rounds(
                                            name, tournament_name)))

    def replace_rounds_list_dict_to_instance(self, list_round, tournament_name):
        new_list = []
        for rounds_dict in list_round:
            new_list.append(self.load_round_to_tournament(rounds_dict["name"], tournament_name))
        return new_list

    def register_and_load_round_to_tournament(self, name, tournament_name):
        self.register_round(name, tournament_name)
        return self.load_round_to_tournament(name, tournament_name)

    def save_list_round_to_database(self, tournament_name, list_rounds):
        self.manager_main.manager_insert.insert_rounds_to_tournament_to_database(
            tournament_name,
            self.manager_main.manager_format.format_update_rounds_to_tournament_to_database(list_rounds))

    def round_keep_running(): # à modifier plus tard
        answer = input("1 pour quitter, 2 pour continuer")
        if answer == "1":
            return False
        elif answer == "2":
            return True

    round_keep_running = staticmethod(round_keep_running)



"""
class ControlRound:
    def __init__(self, manager, match_control):
        self.round = Round
        self.manager = manager
        self.match_control = match_control

    def init_round(self, round_number):
        return self.round(round_number, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def add_date_tournoi(self, tournoi_number, dates):
        if dates not in self.manager.list_all_tournoi[tournoi_number-1].date:
            self.manager.list_all_tournoi[tournoi_number-1].date.append(dates)

    def add_round(self, tournoi_number, round_number):
        print(f"Début du Round{round_number}")
        self.manager.list_all_tournoi[tournoi_number-1].round.append(self.init_round(round_number))
        self.add_date_tournoi(
            tournoi_number,
            datetime.datetime.strptime(
                self.manager.list_all_tournoi[tournoi_number-1].round[
                    round_number-1].start_time, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"))

    # Round : print les matchs restants demandant un résultat
    def show_match_to_record(self, tournoi_number, round_number):
        for matching in self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            if not matching.result_match:
                print(matching)

    def show_match_end(self, tournoi_number, round_number):
        print(f"Round{round_number} terminé le", self.manager.list_all_tournoi[
            tournoi_number-1].round[round_number-1].end_time)
        for matching in self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            print(matching)

    def first_round(self, tournoi_number, round_number):
        shuffled_list = self.manager.list_all_tournoi[tournoi_number-1].player_list
        random.shuffle(shuffled_list)
        for y in range(int(len(shuffled_list) / 2)):
            self.match_control.add_match(
                tournoi_number, round_number, y + 1, shuffled_list[y],
                shuffled_list[y + (int(len(shuffled_list) / 2))])

    def other_round(self, tournoi_number, round_number):
        sorted_by_round_point = sorted(
            self.manager.list_all_tournoi[tournoi_number-1].player_list, key=lambda x: x.round_point, reverse=True)
        sorted_by_round_point_extend = sorted_by_round_point
        sorted_by_round_point_extend.append("Out")
        for y in range(int(len(sorted_by_round_point) / 2)):
            self.match_control.add_match(
                tournoi_number, round_number, y + 1,
                self.test_player1_matches_round(sorted_by_round_point_extend, tournoi_number, round_number),
                self.test_player2_matches_round(sorted_by_round_point_extend, tournoi_number, round_number))

    # Vérifie si la liste match de ce round existe
    def test_player1_matches_round(self, list_played, tournoi_number, round_number):
        if self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            return self.test_player1_in_round(list_played, tournoi_number, round_number)
        else:
            return list_played[0]

    # Vérifie si le joueur est déjà dans un match du round
    def test_player1_in_round(self, list_played, tournoi_number, round_number):
        for player in list_played:
            if self.test_player_in_round_incept(player, tournoi_number, round_number) is False:
                pass
            else:
                return player

    def test_player2_matches_round(self, list_played, tournoi_number, round_number):
        if self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            return self.test_player2_in_round(list_played, tournoi_number, round_number)
        else:
            for player in list_played:
                if player == self.test_player1_matches_round(list_played, tournoi_number, round_number):
                    pass
                elif player in self.test_player1_matches_round(list_played, tournoi_number, round_number).encountered:
                    pass      
                else:
                    return player

    def test_player2_in_round(self, list_played, tournoi_number, round_number):
        for player in list_played:
            if player == "Out":
                for players in list_played:
                    if self.test_player_in_round_incept(players, tournoi_number, round_number) is False:
                        pass
                    elif players == self.test_player1_matches_round(list_played, tournoi_number, round_number):
                        pass
                    else:
                        return players
            elif self.test_player_in_round_incept(player, tournoi_number, round_number) is False:
                pass
            elif player == self.test_player1_matches_round(list_played, tournoi_number, round_number):
                pass
            elif player in self.test_player1_matches_round(list_played, tournoi_number, round_number).encountered:
                pass
            else:
                return player

    def test_player_in_round_incept(self, player, tournoi_number, round_number):
        for matching in self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            if player == matching.player1 or player == matching.player2:
                return False

    def init_round_point(self, tournoi_number):
        for player in self.manager.list_all_tournoi[tournoi_number-1].player_list:
            player.round_point = 0
            player.encountered = []
            self.calcul_round_point(tournoi_number, player)

    def calcul_round_point(self, tournoi_number, player):
        for rounding in self.manager.list_all_tournoi[tournoi_number-1].round:
            for matching in rounding.match:
                if player == matching.result_match[0][0]:
                    player.round_point += matching.result_match[0][1]
                    player.encountered.append(matching.result_match[1][0])
                elif player == matching.result_match[1][0]:
                    player.round_point += matching.result_match[1][1]
                    player.encountered.append(matching.result_match[0][0])

    def test_end_time_register(self, tournoi_number, round_number):
        if self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].end_time:
            return True
        else:
            return False

    def register_end_time(self, tournoi_number, round_number):
        self.manager.list_all_tournoi[tournoi_number - 1].round[round_number - 1].end_time = \
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.add_date_tournoi(
            tournoi_number,
            datetime.datetime.strptime(
                self.manager.list_all_tournoi[tournoi_number - 1].round[
                    round_number - 1].end_time, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"))

    def test_all_scores_register(self, tournoi_number, round_number):
        for matching in self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            if not matching.result_match:
                return False
        return True

    # Round : initialise les instances de matchs dans round.match et print les matchs en question demandant un résultat
    def run_round(self, tournoi_number, round_number):
        if round_number == 1:
            self.first_round(tournoi_number, round_number)
        else:
            self.other_round(tournoi_number, round_number)

    # Round : Conditionne l'emploi des fonctions init et show en fonction du fait qu'init est déjà eu lieu ou non
    def test_round(self, tournoi_number, round_number):
        if not self.manager.list_all_tournoi[tournoi_number-1].round[round_number-1].match:
            self.init_round_point(tournoi_number) # ici
            self.run_round(tournoi_number, round_number)
            self.show_match_to_record(tournoi_number, round_number)
        else:
            if self.test_all_scores_register(tournoi_number, round_number):
                if self.test_end_time_register(tournoi_number, round_number):
                    self.show_match_end(tournoi_number, round_number)
                else:
                    self.register_end_time(tournoi_number, round_number)
                    self.show_match_end(tournoi_number, round_number)
            else:
                self.show_match_to_record(tournoi_number, round_number)

    def load_round_by_name(self, i):
        for v in range(len(self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round[i].match)):
            self.manager.list_all_tournoi[len(
                self.manager.list_all_tournoi)-1].round[i].match[v] = self.match_control.match(
                **self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round[i].match[v])
            self.link_player1_match(
                self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round[i].match[v].player1, i, v)
            self.link_player2_match(
                self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round[i].match[v].player2, i, v)
            self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round[i].match[v].result_match = \
                (self.manager.list_all_tournoi[len(
                    self.manager.list_all_tournoi) - 1].round[i].match[v].result_match[0],
                 self.manager.list_all_tournoi[len(
                     self.manager.list_all_tournoi) - 1].round[i].match[v].result_match[1])
            self.manager.list_all_tournoi[len(
                self.manager.list_all_tournoi) - 1].round[i].match[v].result_match[0][0] = \
                self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round[i].match[v].player1
            self.manager.list_all_tournoi[len(
                self.manager.list_all_tournoi) - 1].round[i].match[v].result_match[1][0] = \
                self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round[i].match[v].player2

    def load_round_by_id(self, i):
        for v in range(len(self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round[i].match)):
            self.manager.list_all_tournoi[len(
                self.manager.list_all_tournoi)-1].round[i].match[v] = self.match_control.match(
                **self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round[i].match[v])
            self.link_player1_match(
                self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round[i].match[v].player1, i, v)
            self.link_player2_match(
                self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round[i].match[v].player2, i, v)
            self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round[i].match[v].result_match = \
                (self.manager.list_all_tournoi[len(
                    self.manager.list_all_tournoi) - 1].round[i].match[v].result_match[0],
                 self.manager.list_all_tournoi[len(
                     self.manager.list_all_tournoi) - 1].round[i].match[v].result_match[1])
            self.manager.list_all_tournoi[len(
                self.manager.list_all_tournoi) - 1].round[i].match[v].result_match[0][0] = \
                self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round[i].match[v].player1
            self.manager.list_all_tournoi[len(
                self.manager.list_all_tournoi) - 1].round[i].match[v].result_match[1][0] = \
                self.manager.list_all_tournoi[len(self.manager.list_all_tournoi) - 1].round[i].match[v].player2

    def link_player1_match(self, plyer, i, v):
        if not self.manager.link_player_class(plyer):
            pass
        else:
            self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round[i].match[v].player1 = \
                self.manager.link_player_class(plyer)

    def link_player2_match(self, plyer, i, v):
        if not self.manager.link_player_class(plyer):
            pass
        else:
            self.manager.list_all_tournoi[len(self.manager.list_all_tournoi)-1].round[i].match[v].player2 = \
                self.manager.link_player_class(plyer)

    def adjust_result_match(self):
        pass
"""