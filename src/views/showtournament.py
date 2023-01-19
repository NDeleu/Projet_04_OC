
class ShowTournament:
    def __init__(self):
        self.name_len_min = 3
        self.name_len_max = 12
        self.location_len_min = 2
        self.location_len_max = 12
        self.time_control_list = [1, 2, 3]
        self.number_round_choice = [1, 2]
        self.number_round_number = [4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.description_choice = [1, 2]
        self.description_len_min = 1
        self.description_len_max = 42

    def init_dict_tournament_register(name, location, time_control, number_round, description):
        return {"name": name,
                "location": location,
                "time_control": time_control,
                "number_round": number_round,
                "description": description}

    init_dict_tournament_register = staticmethod(init_dict_tournament_register)

    def init_name_tournament_register():
        print("Veuillez saisir le nom du tournoi")

    init_name_tournament_register = staticmethod(init_name_tournament_register)