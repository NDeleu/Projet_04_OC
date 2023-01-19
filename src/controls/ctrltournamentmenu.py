from src.views.shownavigatetournamentmenu import ShowNavigateTournamentMenu


class CtrlTournamentMenu:
    def __init__(self):
        self.show_navigate_tournament_menu = ShowNavigateTournamentMenu()

    def quit_tournament(name_tournament):
        return f"Vous avez quitté le tournoi nommé {name_tournament}."

    quit_tournament = staticmethod(quit_tournament)
