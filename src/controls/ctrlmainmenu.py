from src.views import ShowNavigateMainMenu


class CtrlMainMenu:
    def __init__(self, view_main):
        self.show_navigate_main_menu = ShowNavigateMainMenu()
        self.view_main = view_main

    def menu_navigate(self):
        self.show_navigate_main_menu.show_menu_navigate()
        answer = self.view_main.view_input.try_choice_input(self.show_navigate_main_menu.list_choice)
        if answer == "1":
            # create tournament
            print("\nLa fonction de création de tournoi n'est pas encore implantée.")
        elif answer == "2":
            # create player
            print("\nLa fonction de création de joueurs n'est pas encore implantée.")
        elif answer == "3":
            # load tournament
            print("\nLa fonction de chargement et lancement de tournoi n'est pas encore implantée.")
        elif answer == "4":
            # pandas
            print("\nLa fonction de consultation des résultats, "
                  "tournois, rounds, matchs et joueurs n'est pas encore implantée.")
        elif answer == "5":
            # flake8
            print("\nLa fonction de consultation du flake8 n'est pas encore implantée")
        elif answer == "6":
            # change result matches
            print("\nLa fonction de modification des matchs n'est pas encore implantée")
        elif answer == "7":
            # leave application
            return False
        else:
            # erreur commande
            print("\nerreur de saisie")
            pass
