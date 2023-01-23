
class ShowTournament:

    def init_name_tournament_register(len_min, len_max):
        return f"Veuillez saisir le nom du tournoi. \n" \
               f"Ce nom doit être unique," \
               f"soit ne pas être utilisé par un autre tournoi enregistré dans la base de donnée. \n" \
               f"Il doit être composé au minimum de {len_min} caractères et au maximum de {len_max} caractères"

    init_name_tournament_register = staticmethod(init_name_tournament_register)

    def init_location_tournament_register(len_min, len_max):
        return f"Veuillez saisir le lieu du tournoi. \n" \
               f"Il doit être composé au minimum de {len_min} caractères et au maximum de {len_max} caractères"

    init_location_tournament_register = staticmethod(init_location_tournament_register)

    def init_time_control_tournament_register():
        return "Veuillez choisir le type de contrôle du temps que vous désirez pour les matchs de ce tournoi : \n" \
               "Blitz :          1 \n" \
               "Coup Rapide :    2 \n" \
               "Bullet :         3 "

    init_time_control_tournament_register = staticmethod(init_time_control_tournament_register)

    def init_number_round_choice_tournament_register():
        return "Désirez vous laisser le nombre de rounds par défaut à quatre ? (Recommandé) : \n" \
               "Oui :    1 \n" \
               "Non :    2 "

    init_number_round_choice_tournament_register = staticmethod(init_number_round_choice_tournament_register)

    def init_number_round_wanted_tournament_register():
        return "Veuillez saisir le nombre de rounds désiré pour ce tournoi. "

    init_number_round_wanted_tournament_register = staticmethod(init_number_round_wanted_tournament_register)

    def init_description_choice_tournament_register():
        return "Désirez vous ajouter une description à ce tournoi ? : \n" \
               "Oui :    1 \n" \
               "Non :    2 "

    init_description_choice_tournament_register = staticmethod(init_description_choice_tournament_register)

    def init_description_string_tournament_register(len_min, len_max):
        return f"Veuillez saisir la description que vous souhaitez joindre à ce tournoi. \n" \
               f"Elle doit être composée au minimum de {len_min} caractères et au maximum de {len_max} caractères"

    init_description_string_tournament_register = staticmethod(init_description_string_tournament_register)

    def validate_creation_tournament(tournament_inst):
        return f"Le tournoi nommé {tournament_inst} a bien été créé et enregistré dans la base de donnée"

    validate_creation_tournament = staticmethod(validate_creation_tournament)