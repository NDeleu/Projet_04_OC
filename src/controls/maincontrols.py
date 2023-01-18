from src.controls.ctrlrelationclass import CtrlRelationClass


class MainControls:
    def __init__(self):
        self.relation_class = CtrlRelationClass()
        self.running = True
        self.tournament_running = False
        self.loaded_tournament = None

    def main_run(self):
        while self.running:
            if self.tournament_running:
                # lancement du tournoi chargé
                pass
            else:
                self.control_main_menu()

    def control_main_menu(self):
        self.relation_class.main_menu.show_navigate_main_menu.show_menu_navigate()
        record = self.relation_class.view_main.view_input.number_choice_input()
        if record == "7":
            self.relation_class.main_menu.show_navigate_main_menu.show_leave_app()
            self.running = False
        else:
            self.relation_class.main_menu.menu_navigate(record)

