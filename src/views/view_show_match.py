
class ShowMatch:
    def __init__(self):
        pass

    def show_init_enter_result_match():
        return "Veuillez saisir le choix correspondant " \
               "au résultat du match : \n"

    show_init_enter_result_match = staticmethod(show_init_enter_result_match)

    def show_enter_result_match(player1, player2):
        return f"{player1} gagnant :    1 \n" \
               f"{player2} gagnant :    2 \n" \
               f"Égalité :              3 \n"

    show_enter_result_match = staticmethod(show_enter_result_match)

    def show_init_choice_match():
        return "Veuillez saisir le choix correspondant au match pour " \
               "lequel vous souhaitez saisir un résultat : \n"

    show_init_choice_match = staticmethod(show_init_choice_match)

    def show_choice_match_to_change(round_name, match_res, number_choice):
        return f"{round_name} : {match_res} :      {number_choice} \n"

    show_choice_match_to_change = staticmethod(show_choice_match_to_change)

    def show_choice_match_to_change_leave(number_choice):
        return f"Retour au menu principal :         " \
               f"                   {number_choice} \n"

    show_choice_match_to_change_leave = staticmethod(
        show_choice_match_to_change_leave)

    def confirm_result_match_register(result_match):
        return f"{result_match} a bien été enregistré \n"

    confirm_result_match_register = staticmethod(confirm_result_match_register)

    def init_show_result_match(result_match):
        return f"{result_match} \n"

    init_show_result_match = staticmethod(init_show_result_match)
