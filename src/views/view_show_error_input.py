
class ShowErrorInput:

    def error_choice_input():
        return "ERREUR : Cette entrée n'est pas attribuée à une action possible ou existante.\n" \
               "Merci de saisir un numéro relatif à une action proposée ci dessus :"

    error_choice_input = staticmethod(error_choice_input)

    def error_value_num_input():
        return "ERREUR : Cette entrée ne correspond pas au format attendu. \nMerci de saisir une valeur numérique."

    error_value_num_input = staticmethod(error_value_num_input)

    def error_value_alphanum_input():
        return "\nERREUR : Cette entrée ne correspond pas au format attendu. \n" \
               "Merci de saisir une valeur alphanumérique. \n"

    error_value_alphanum_input = staticmethod(error_value_alphanum_input)

    def error_already_exists(type_item, name_instance):
        return f"\nERREUR : Les données : {type_item} : {name_instance} existe déjà dans la base de donnée. \n" \
               f"Merci de saisir une valeur distincte. \n"

    error_already_exists = staticmethod(error_already_exists)

    def error_not_exists(type_item, name_instance):
        return f"\nERREUR : Les données {type_item} : {name_instance} n'existe pas dans la base de donnée. \n" \
               f"Merci de saisir une valeur reconnue. \n" \
               f"Vous pouvez à cette fin consulter la base de donnée depuis le menu principal \n"

    error_not_exists = staticmethod(error_not_exists)

    def error_not_enough_characters(len_min):
        return f"\nERREUR : Cette entrée ne possède pas assez de caractères. \n" \
               f"Merci de saisir une entrée avec pour minimum : {len_min} caractères \n"

    error_not_enough_characters = staticmethod(error_not_enough_characters)

    def error_too_many_characters(len_max):
        return f"\nERREUR : Cette entrée possède trop de caractères. \n" \
               f"Merci de saisir une entrée avec pour maximum : {len_max} caractères \n"

    error_too_many_characters = staticmethod(error_too_many_characters)

    def error_id_player_input():
        return "\nERREUR : Cette entrée ne correspond pas au format attendu.\n" \
               "Merci de saisir des chiffres pour les deux premiers caractères, \n" \
               "puis des lettres pour les quatre caractères suivants \n"

    error_id_player_input = staticmethod(error_id_player_input)

    def error_date_input():
        return "\nERREUR : Cette entrée ne correspond pas au format attendu. \n" \
               "Merci de saisir un format date tels que AAAA-MM-JJ. \n" \
               "Exemple pour le 02 Mars 1978 : 1978-03-02 \n"

    error_date_input = staticmethod(error_date_input)

    def error_record():
        return "Une erreur est survenue lors de la création et l'enregistrement des données. \n" \
               "Veuillez réitérer l'opération. Si le problème persiste, veuillez contacter le développeur"

    error_record = staticmethod(error_record)