
class ShowTournament:

    def init_name_tournament_register(len_min, len_max):
        return f"Veuillez saisir le nom du tournoi. \n" \
               f"Ce nom doit être unique," \
               f"soit ne pas être utilisé par un autre tournoi " \
               f"enregistré dans la base de donnée. \n" \
               f"Il doit être composé au minimum de {len_min} " \
               f"caractères et au maximum de {len_max} caractères"

    init_name_tournament_register = staticmethod(init_name_tournament_register)

    def init_location_tournament_register(len_min, len_max):
        return f"Veuillez saisir le lieu du tournoi. \n" \
               f"Il doit être composé au minimum de {len_min} " \
               f"caractères et au maximum de {len_max} caractères"

    init_location_tournament_register = staticmethod(
        init_location_tournament_register)

    def init_time_control_tournament_register():
        return "Veuillez choisir le type de contrôle du temps " \
               "que vous désirez pour les matchs de ce tournoi : \n" \
               "Blitz :          1 \n" \
               "Coup Rapide :    2 \n" \
               "Bullet :         3 "

    init_time_control_tournament_register = staticmethod(
        init_time_control_tournament_register)

    def init_number_round_choice_tournament_register():
        return "Désirez vous laisser le nombre de rounds " \
               "par défaut à quatre ? (Recommandé) : \n" \
               "Oui :    1 \n" \
               "Non :    2 "

    init_number_round_choice_tournament_register = staticmethod(
        init_number_round_choice_tournament_register)

    def init_number_round_wanted_tournament_register():
        return "Veuillez saisir le nombre de rounds désiré pour ce tournoi. "

    init_number_round_wanted_tournament_register = staticmethod(
        init_number_round_wanted_tournament_register)

    def init_description_choice_tournament_register():
        return "Désirez vous ajouter une description à ce tournoi ? : \n" \
               "Oui :    1 \n" \
               "Non :    2 "

    init_description_choice_tournament_register = staticmethod(
        init_description_choice_tournament_register)

    def init_description_string_tournament_register(len_min, len_max):
        return f"Veuillez saisir la description que " \
               f"vous souhaitez joindre à ce tournoi. \n" \
               f"Elle doit être composée au minimum de {len_min} " \
               f"caractères et au maximum de {len_max} caractères"

    init_description_string_tournament_register = staticmethod(
        init_description_string_tournament_register)

    def validate_creation_tournament(tournament_inst):
        return f"Le tournoi nommé {tournament_inst} a " \
               f"bien été créé et enregistré dans la base de donnée"

    validate_creation_tournament = staticmethod(validate_creation_tournament)

    def init_load_tournament(len_min, len_max):
        return f"Veuillez saisir le nom du tournoi que " \
               f"vous souhaitez charger. \n" \
               f"Il doit être composé au minimum de {len_min} " \
               f"caractères et au maximum de {len_max} caractères"

    init_load_tournament = staticmethod(init_load_tournament)

    def show_load_id_player_to_tournament():
        return "Veuillez saisir l'identifiant du joueur " \
               "que vous souhaitez intégrer au tournoi. \n" \
               "Il doit être composé de six caractères. \n" \
               "Des chiffres pour les deux premiers caractères. \n" \
               "Des lettres pour les quatre derniers caractères."

    show_load_id_player_to_tournament = staticmethod(
        show_load_id_player_to_tournament)

    def show_choice_id_player_to_tournament():
        return "Désirez vous : \n" \
               "Charger un joueur préexistant dans la base " \
               "de donnée et l'ajouter au tournoi :  1 \n" \
               "Créer un joueur dans la base de donnée et " \
               "l'ajouter au tournoi :                2"

    show_choice_id_player_to_tournament = staticmethod(
        show_choice_id_player_to_tournament)

    def show_error_check_player_in_player_list_tournament():
        return "Le joueur est déjà inscrit dans le tournoi actuel. \n" \
               "Veuillez renseigner l'identifiant d'un autre joueur"

    show_error_check_player_in_player_list_tournament = staticmethod(
        show_error_check_player_in_player_list_tournament)

    def show_no_player_in_list_player():
        return "Veuillez inscrire 8 joueurs participants au tournoi. \n" \
               "Il n'y a actuellement aucun joueur inscrits dans ce tournoi."

    show_no_player_in_list_player = staticmethod(show_no_player_in_list_player)

    def show_not_enough_player_in_list_player(player_list):
        return f"Veuillez inscrire 8 joueurs participants au tournoi. \n" \
               f"Il y a actuellement {len(player_list)} joueurs inscrits. \n" \
               f"Voici la liste des joueurs participants : \n"

    show_not_enough_player_in_list_player = staticmethod(
        show_not_enough_player_in_list_player)

    def show_completed_player_in_list_player():
        return "Les 8 joueurs participants ont " \
               "étés enregistrés pour ce tournoi. \n" \
               "Voici la liste des joueurs participants : \n"

    show_completed_player_in_list_player = staticmethod(
        show_completed_player_in_list_player)

    def show_all_player_in_list_player(list_player):
        for player in list_player:
            print(player)

    show_all_player_in_list_player = staticmethod(
        show_all_player_in_list_player)

    def show_success_add_player():
        return "Le joueur a bien été enregistré " \
               "comme participant à ce tournoi."

    show_success_add_player = staticmethod(show_success_add_player)

    def show_end_tournament(tournament_name, date_end):
        return f"Fin du Tournoi : {tournament_name} le {date_end} \n"

    show_end_tournament = staticmethod(show_end_tournament)

    def show_init_result_end_tournament():
        return "Classement et résultats des joueurs : \n"

    show_init_result_end_tournament = staticmethod(
        show_init_result_end_tournament)

    def show_result_end_tournament(player_name, player_surname,
                                   player_id, player_round_point):
        return f"{player_name} {player_surname} " \
               f"{player_id} :   {player_round_point}"

    show_result_end_tournament = staticmethod(show_result_end_tournament)
