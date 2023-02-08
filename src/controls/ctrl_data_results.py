from src.views.view_show_data_results import ShowDataResults
import pandas
import os


class CtrlDataResults:
    def __init__(
            self, view_main, manager_main,
            player_methods, tournament_methods):
        self.df = pandas.DataFrame
        self.os = os
        self.show_data_results = ShowDataResults
        self.view_main = view_main
        self.manager_main = manager_main
        self.player_methods = player_methods
        self.tournament_methods = tournament_methods
        self.list_answer_choice_show_data_results = [1, 2]
        self.list_answer_choice_select_data_results = [1, 2, 3, 4, 5, 6]
        self.cd = "../Projet_04_OC/data_results/"

    def choice_show_data_results(self):
        print(self.show_data_results.show_choice_show_data_results())
        answer_show = self.view_main.view_input.try_choice_input(
            self.list_answer_choice_show_data_results)
        if answer_show == "1":
            answer_receive = self.choice_choice_select_data_results()
            if answer_receive is False:
                pass
            else:
                if type(answer_receive[2]) is str:
                    print(answer_receive[1])
                    print(self.show_data_results.empty_dataframe())
                else:
                    print(answer_receive[1])
                    print(answer_receive[2])
        elif answer_show == "2":
            self.check_repository_data_exists()
            answer_receive = self.choice_choice_select_data_results()
            if answer_receive is False:
                pass
            else:
                if type(answer_receive[2]) is str:
                    print(answer_receive[1])
                    print(self.show_data_results.empty_dataframe())
                else:
                    translate_html = answer_receive[2].to_html()
                    record_html = open(
                        f"{self.cd}{answer_receive[0]}",
                        "w")
                    record_html.write(translate_html)
                    record_html.close()
                    if not self.os.path.exists(
                            f"{self.cd}{answer_receive[0]}"):
                        print(self.show_data_results.error_record_data_html())
                    else:
                        print(self.show_data_results.success_record_data_html(
                            answer_receive[1], answer_receive[0]))

    def choice_choice_select_data_results(self):
        print(self.show_data_results.show_choice_select_data_results())
        answer_select = self.view_main.view_input.try_choice_input(
            self.list_answer_choice_select_data_results)
        if answer_select == "1":
            return self.player_list_by_alpha_order()
        elif answer_select == "2":
            return self.player_list_by_ranking_order()
        elif answer_select == "3":
            return self.tournament_list()
        elif answer_select == "4":
            return self.tournament_description()
        elif answer_select == "5":
            return self.tournament_players_list()
        elif answer_select == "6":
            return self.tournament_rounds_list()

    def player_list_by_alpha_order(self):
        dict_players = self.manager_main.\
            manager_format.format_data_results_all_players(
                self.manager_main.
                check_main.check_models.open_list_all_player_dict())
        return "player_list_by_alpha.html", \
               self.show_data_results.show_player_list_by_alpha_order(), \
               self.df.transpose(self.df(dict_players)).sort_values(
                   by=["name"])

    def player_list_by_ranking_order(self):
        dict_players = self.manager_main.\
            manager_format.format_data_results_all_players(
                self.manager_main.
                check_main.check_models.open_list_all_player_dict())
        return "player_list_by_ranking.html", \
               self.show_data_results.show_player_list_by_ranking_order(), \
               self.df.transpose(self.df(dict_players)).sort_values(
                   by=["total_points"], ascending=False)

    def tournament_list(self):
        dict_tournament = self.manager_main.\
            manager_format.format_data_results_all_tournaments(
                self.manager_main.
                check_main.check_models.open_list_all_tournament_dict())
        return "tournament_list.html", \
               self.show_data_results.show_tournament_list(), \
               self.df.transpose(self.df(dict_tournament))

    def tournament_description(self):
        tournament_name = self.tournament_methods.load_tournament()
        if tournament_name is None:
            return False
        else:
            dict_tournament_describe = self.manager_main.\
                check_main.check_models.open_tournament_description(
                    tournament_name)
            return f"tournament_description_{tournament_name}.html", \
                   self.show_data_results.show_tournament_description(
                       tournament_name), \
                   self.df.transpose(self.df(dict_tournament_describe))

    def tournament_players_list(self):
        tournament_name = self.tournament_methods.load_tournament()
        if tournament_name is None:
            return False
        else:
            dict_tournament_player_list = self.manager_main.\
                manager_format.format_data_results_player_list_tournament(
                    self.manager_main.
                    check_main.check_models.open_tournament_player_list(
                        tournament_name))
            if not dict_tournament_player_list:
                return f"tournament_players_list_{tournament_name}.html", \
                       self.show_data_results.show_tournament_players_list(
                           tournament_name), \
                       self.show_data_results.\
                           show_empty_tournament_players_list(tournament_name)
            else:
                return f"tournament_players_list_{tournament_name}.html", \
                       self.show_data_results.show_tournament_players_list(
                           tournament_name), \
                       self.df.transpose(self.df(dict_tournament_player_list))

    def tournament_rounds_list(self):
        tournament_name = self.tournament_methods.load_tournament()
        if tournament_name is None:
            return False
        else:
            dict_tournament_rounds_list = self.manager_main.\
                check_main.check_models.open_tournament_round_match_list(
                    tournament_name)
            if not dict_tournament_rounds_list:
                return f"tournament_rounds_list_{tournament_name}.html", \
                       self.show_data_results.show_tournament_rounds_list(
                           tournament_name), \
                       self.show_data_results.\
                           show_empty_tournament_rounds_list(tournament_name)
            else:
                return f"tournament_rounds_list_{tournament_name}.html", \
                       self.show_data_results.show_tournament_rounds_list(
                           tournament_name), \
                       self.df(dict_tournament_rounds_list)

    def check_repository_data_exists(self):
        if not self.os.path.exists(self.cd):
            self.os.makedirs(self.cd)
        else:
            pass
