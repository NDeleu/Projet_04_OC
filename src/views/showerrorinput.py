
class ShowErrorInput:

    def error_choice_input():
        return "Cette entrée n'est pas attribuée à une action possible ou existante.\n" \
               "Merci de saisir un numéro relatif à une action proposée ci dessus :"

    error_choice_input = staticmethod(error_choice_input)

    def error_value_num_input():
        return "Cette entrée ne correspond pas au format attendu. \nMerci de saisir une valeur numérique."

    error_value_num_input = staticmethod(error_value_num_input)

    def error_value_alphanum_input():
        return "Cette entrée ne correspond pas au format attendu. \nMerci de saisir une valeur alphanumérique."

    error_value_alphanum_input = staticmethod(error_value_alphanum_input)

    def error_already_exists(type_item, name_instance):
        return f"Les données : {type_item} : {name_instance} existe déjà dans la base de donnée. \n" \
               f"Merci de saisir une valeur distincte."

    error_already_exists = staticmethod(error_already_exists)

    def error_not_exists(type_item, name_instance):
        return f"Les données {type_item} : {name_instance} n'existe pas dans la base de donnée. \n" \
               f"Merci de saisir une valeur reconnue."

    error_not_exists = staticmethod(error_not_exists)

    def error_not_enough_characters(len_min):
        return f"Cette entrée ne possède pas assez de caractères. \n" \
               f"Merci de saisir une entrée avec pour minimum : {len_min} caractères"

    error_not_enough_characters = staticmethod(error_not_enough_characters)

    def error_too_many_characters(len_max):
        return f"Cette entrée possède trop de caractères. \n" \
               f"Merci de saisir une entrée avec pour maximum : {len_max} caractères"

    error_too_many_characters = staticmethod(error_too_many_characters)

    def error_id_player_input():
        return "Cette entrée ne correspond pas au format attendu.\n" \
               "Merci de saisir des chiffres pour les deux premiers caractères, \n" \
               "puis des lettres pour les quatre caractères suivants"

    error_id_player_input = staticmethod(error_id_player_input)

    def error_date_input():
        return "Cette entrée ne correspond pas au format attendu. \n" \
               "Merci de saisir un format date tels que AAAA-MM-JJ. \n" \
               "Exemple pour le 02 Mars 1978 : 1978-03-02"

    error_date_input = staticmethod(error_date_input)
