from src.views import ShowNavigateMainMenu


class CtrlMainMenu:
    def __init__(self, view_main, tournament_running, player_method):
        self.show_navigate_main_menu = ShowNavigateMainMenu()
        self.view_main = view_main
        self.tournament_running = tournament_running
        self.player_method = player_method

    def menu_navigate(self):
        self.show_navigate_main_menu.show_menu_navigate()
        answer = self.view_main.view_input.try_choice_input(self.show_navigate_main_menu.list_choice)
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
            print("\nLa fonction de consultation des résultats, "
                  "tournois, rounds, matchs et joueurs n'est pas encore implantée.")
        elif answer == "5":
            # flake8
            print("\nLa fonction de consultation du flake8 n'est pas encore implantée")
        elif answer == "6":
            # change result matches
            tournament_name = self.tournament_running.tournament_methods.load_tournament()
            if tournament_name is None:
                print(self.view_main.view_input.show_error_input.error_tournament_name(tournament_name))
            else:
                self.tournament_running.round_running.match_methods.change_and_save_result_match(tournament_name)
        elif answer == "7":
            # leave application
            return False
        else:
            # erreur commande
            print("\nerreur de saisie")
            pass
