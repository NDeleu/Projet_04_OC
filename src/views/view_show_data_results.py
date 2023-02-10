
class ShowDataResults:

    def show_choice_show_data_results():
        return "\nVeuillez choisir le type d'affichage désiré " \
               "pour la data :\n" \
               "Afficher la data sur console :      1\n" \
               "Créer un fichier exportable HTML :  2"

    show_choice_show_data_results = staticmethod(
        show_choice_show_data_results)

    def show_choice_select_data_results():
        return "\nVeuillez choisir le type de data désiré : \n" \
               "La liste des joueurs par ordre alphabétique :       1\n" \
               "La liste des joueurs par classement :               2\n" \
               "La liste de tous les tournois :                     3\n" \
               "Le descriptif d'un tournoi donné :                  4\n" \
               "La liste des joueurs d'un tournoi donné :           5\n" \
               "La liste des rounds et des matchs\n " \
               "relatifs d'un tournoi donné :                      6\n"

    show_choice_select_data_results = staticmethod(
        show_choice_select_data_results)

    def show_player_list_by_alpha_order():
        return "Liste des joueurs par ordre alphabétique"

    show_player_list_by_alpha_order = staticmethod(
        show_player_list_by_alpha_order)

    def show_player_list_by_ranking_order():
        return "Liste des joueurs par classement"

    show_player_list_by_ranking_order = staticmethod(
        show_player_list_by_ranking_order)

    def show_tournament_list():
        return "Liste de tous les tournois"

    show_tournament_list = staticmethod(
        show_tournament_list)

    def show_tournament_description(tournament_name):
        return f"Détails du tournoi : {tournament_name}"

    show_tournament_description = staticmethod(
        show_tournament_description)

    def show_tournament_players_list(tournament_name):
        return f"Liste des joueurs participants au tournoi : {tournament_name}"

    show_tournament_players_list = staticmethod(
        show_tournament_players_list)

    def show_tournament_rounds_list(tournament_name):
        return f"Liste des rounds " \
               f"et matchs relatifs du tournoi : {tournament_name}"

    show_tournament_rounds_list = staticmethod(
        show_tournament_rounds_list)

    def show_empty_tournament_players_list(tournament_name):
        return f"Aucun Joueur n'est enregistré " \
               f"dans le tournoi : {tournament_name}"

    show_empty_tournament_players_list = staticmethod(
        show_empty_tournament_players_list)

    def show_empty_tournament_rounds_list(tournament_name):
        return f"Aucun Round n'est enregistré " \
               f"dans le tournoi : {tournament_name}"

    show_empty_tournament_rounds_list = staticmethod(
        show_empty_tournament_rounds_list)

    def empty_dataframe():
        return "N'ayant aucun attribut a relever dans le dataframe\n " \
               "aucun fichier html relatif ne sera " \
               "créé suite à cette opération.\n"

    empty_dataframe = staticmethod(empty_dataframe)

    def error_record_data_html():
        return "Une erreur est survenue lors de la création " \
               "du fichier html.\n" \
               "Veuillez réitérer l'opération.\n" \
               "Si le problème perssiste, merci de contacter le développeur\n"

    error_record_data_html = staticmethod(error_record_data_html)

    def success_record_data_html(subject, html_name):
        return f"Le fichier html : {subject} a été créé.\n" \
               f"Vous pouvez le consulter directement " \
               f"dans le dossier data_results.\n" \
               f"A cette fin, merci d'ouvrir le fichier {html_name} " \
               f"dans un navigateur tels que Microsoft Edge, " \
               f"Google Chrome ou encore Mozilla Firefox.\n" \
               f"Pour d'avantage d'informations, " \
               f"merci de vous reporter au README.\n"

    success_record_data_html = staticmethod(success_record_data_html)
