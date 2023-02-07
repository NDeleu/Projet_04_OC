

class ShowPlayer:

    def init_name_player_register(len_min, len_max):
        return f"Veuillez saisir le nom du joueur. \n" \
               f"Il doit être composé au minimum de {len_min} " \
               f"caractères et au maximum de {len_max} caractères"

    init_name_player_register = staticmethod(init_name_player_register)

    def init_surname_player_register(len_min, len_max):
        return f"Veuillez saisir le prénom du joueur. \n" \
               f"Il doit être composé au minimum de {len_min} " \
               f"caractères et au maximum de {len_max} caractères"

    init_surname_player_register = staticmethod(init_surname_player_register)

    def init_id_chess_player_register():
        return "Veuillez saisir l'identifiant du joueur. \n" \
               "Il doit être composé de six caractères. \n" \
               "Des chiffres pour les deux premiers caractères. \n" \
               "Des lettres pour les quatre derniers caractères."

    init_id_chess_player_register = staticmethod(init_id_chess_player_register)

    def init_birthday_player_register():
        return "Veuillez saisir la date de naissance du joueur. \n" \
               "Elle doit être au format AAAA-MM-JJ. \n" \
               "Vous devez saisir aussi les tirets du 6 " \
               "pour délimiter les informations " \
               "comme dans l'exemple donnée.\n" \
               "AAAA correspond à l'année, MM au mois, et JJ au jour."

    init_birthday_player_register = staticmethod(init_birthday_player_register)

    def validate_creation_player(player_inst):
        return f"Le joueur nommé {player_inst} " \
               f"a bien été créé et enregistré dans la base de donnée"

    validate_creation_player = staticmethod(validate_creation_player)
