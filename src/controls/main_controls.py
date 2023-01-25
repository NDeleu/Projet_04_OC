from src.controls.ctrl_relation_class import CtrlRelationClass, LeaveApplication, LeaveTournament


class MainControls:
    def __init__(self):
        self.relation_class = CtrlRelationClass()
        self.running = True
        self.tournament_running = False
        self.loaded_tournament = None
        self.leave_application = LeaveApplication()
        self.leave_tournament = LeaveTournament(self.loaded_tournament)

    def main_run(self):
        while self.running:
            if self.tournament_running:
                # lancement du tournoi chargé
                try: 
                    self.leave_tour(self.relation_class.tournament_running.tournament_run(self.loaded_tournament))
                except LeaveTournament:
                    print(LeaveTournament(self.loaded_tournament))
                    self.tournament_running = False
                    self.loaded_tournament = None
            else:
                try:
                    answer = self.leave_app(self.relation_class.main_menu.menu_navigate())
                    if type(answer) == str:
                        self.loaded_tournament = answer
                        self.tournament_running = True
                    elif answer is None:
                        self.loaded_tournament = answer
                        self.tournament_running = False
                except LeaveApplication:
                    print(self.leave_application)
                    self.running = False

    def leave_app(self, method_tried):
        if method_tried is False:
            raise self.leave_application
        return method_tried

    def leave_tour(self, method_tried):
        if method_tried is False:
            raise self.leave_tournament
        return method_tried

