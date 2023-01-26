from src.controls.ctrl_round_running import CtrlRoundRunning
from src.controls.ctrl_round_methods import CtrlRoundMethods


class CtrlTournamentRunning:
    def __init__(self, tournament_methods):
        self.round_methods = CtrlRoundMethods()
        self.round_running = CtrlRoundRunning()
        self.tournament_methods = tournament_methods
        self.tournament_main = None
        self.tournament_main_running = True

    def tournament_run(self, tournament_name):
        if self.tournament_main_running is False:
            return False
        else:

            self.tournament_main = self.tournament_methods.tournament(**
                                                                      self.tournament_methods.manager_main.check_main.
                                                                      check_models.open_load_tournament(
                                                                          tournament_name))
            print("name : ", self.tournament_main.name)
            print("lieu : ", self.tournament_main.location)
            print("nombre de round : ", self.tournament_main.number_round)

            # Gestion de la liste des joueurs
            if not self.tournament_main.player_list:
                # Message d'instruction sur le manque de joueurs
                self.tournament_methods.no_player_in_list_player()
                # Ajout d'un joueur dans la liste de joueurs du tournoi
                self.tournament_main.player_list.append(
                    self.tournament_methods.player_methods.id_player_to_inst_player_displayed(
                        self.tournament_methods.choice_id_player_to_tournament(self.tournament_main.player_list)))
                # Message confirmant l'ajout du joueur
                self.tournament_methods.success_add_player()
                # Sauvegarde la nouvelle liste de joueurs dans la base de donnée
                self.tournament_methods.save_list_player_to_database(
                    self.tournament_main.name, self.tournament_main.player_list)
            else:
                # Modifie la liste de joueurs de liste de dictionnaire à liste d'instance de classe
                self.tournament_main.player_list = self.tournament_methods.replace_player_list_dict_to_instance(
                    self.tournament_main.player_list)

                if len(self.tournament_main.player_list) < 8:
                    # Message d'instruction sur le manque de joueurs
                    self.tournament_methods.not_enough_player_in_list_player(self.tournament_main.player_list)
                    # Ajout d'un joueur dans la liste de joueurs du tournoi
                    self.tournament_main.player_list.append(
                        self.tournament_methods.player_methods.id_player_to_inst_player_displayed(
                            self.tournament_methods.choice_id_player_to_tournament(self.tournament_main.player_list)))
                    # Message confirmant l'ajout du joueur
                    self.tournament_methods.success_add_player()
                    # Sauvegarde la nouvelle liste de joueurs dans la base de donnée
                    self.tournament_methods.save_list_player_to_database(
                        self.tournament_main.name, self.tournament_main.player_list)
                    # Message en cas de liste des joueurs complétée
                    if len(self.tournament_main.player_list) == 8:
                        self.tournament_methods.completed_player_in_list_player(self.tournament_main.player_list)
                else:
                    pass

            self.tournament_main_running = self.tournament_methods.tournament_keep_running()
