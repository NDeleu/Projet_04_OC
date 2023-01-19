from src.controls.ctrlrelationclass import CtrlRelationClass


class MainControls:
    def __init__(self):
        self.relation_class = CtrlRelationClass()
        self.running = True
        self.tournament_running = False
        self.loaded_tournament = None
        self.leave_application = LeaveApplication()

    def main_run(self):
        while self.running:
            if self.tournament_running:
                # lancement du tournoi chargé
                pass
            else:
                try:
                    self.leave_app(self.relation_class.main_menu.menu_navigate(
                        self.relation_class.view_main.view_input.number_choice_input()))
                except LeaveApplication:
                    print("bye bye")
                    self.running = False

    def leave_app(self, method_tried):
        if method_tried is False:
            raise self.leave_application
        return method_tried


class LeaveApplication(Exception):
    pass

