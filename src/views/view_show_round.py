
class ShowRound:
    def __init__(self):
        pass

    def init_show_result_match():
        return "Résultats des matchs du Round : \n"

    init_show_result_match = staticmethod(init_show_result_match)

    def init_show_end_round(round_name):
        return f"Fin du {round_name}"

    init_show_end_round = staticmethod(init_show_end_round)

    def init_show_create_round(round_name):
        return f"Création du {round_name}"

    init_show_create_round = staticmethod(init_show_create_round)

    def init_resume_round(round_name):
        return f"{round_name}"

    init_resume_round = staticmethod(init_resume_round)
