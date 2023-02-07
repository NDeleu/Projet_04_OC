

class ShowNavigateMainMenu:
    def __init__(self):
        self.list_choice = [1, 2, 3, 4, 5, 6, 7]

    def show_leave_app():
        return "Merci d'avoir utilisé notre gestionnaire " \
               "de tournoi d'échec. \n" \
               "A bientot !"

    show_leave_app = staticmethod(show_leave_app)

    def show_menu_navigate():
        print("\n         Menu Principal          \n")
        print("Créer un nouveau tournoi :                           1")
        print("Créer un nouveau profil de joueur :                  2")
        print("Charger et lance un tournoi existant :               3")
        print("Consulter la base de donnée :                        4")
        print("Consulter le Flake 8 du code :                       5")
        print("Modifier les résultats d'un match existant :         6")
        print("Quitter l'application :                              7\n")

    show_menu_navigate = staticmethod(show_menu_navigate)
