from src.views import ShowNavigateMainMenu


class CtrlMainMenu:
    def __init__(self, view_main, tournament_running,
                 player_method, flake_8, data_results):
        self.show_navigate_main_menu = ShowNavigateMainMenu()
        self.view_main = view_main
        self.tournament_running = tournament_running
        self.player_method = player_method
        self.flake_8 = flake_8
        self.data_results = data_results

    def menu_navigate(self):
        self.show_navigate_main_menu.show_menu_navigate()
        answer = self.view_main.view_input.try_choice_input(
            self.show_navigate_main_menu.list_choice)
        if answer == "1":
            # create tournament
            self.tournament_running.tournament_methods.register_tournament()
        elif answer == "2":
            # create player
            self.player_method.register_player()
        elif answer == "3":
            # load tournament
            return self.tournament_running.tournament_methods.load_tournament()
        elif answer == "4":
            # pandas
            return self.data_results.choice_show_data_results()
        elif answer == "5":
            # flake8
            return self.flake_8.choice_show_flake()
        elif answer == "6":
            # change result matches
            tournament_name = self.tournament_running.\
                tournament_methods.load_tournament()
            if tournament_name is None:
                print(self.view_main.view_input.show_error_input.
                      error_tournament_name(tournament_name))
            else:
                self.tournament_running.round_running.match_methods.\
                    change_and_save_result_match(tournament_name)
                self.player_method.player_total_point_calculated(
                    self.player_method.list_all_player_displayed())
        elif answer == "7":
            # leave application
            return False
        else:
            # erreur commande
            print("\nerreur de saisie")
            pass
