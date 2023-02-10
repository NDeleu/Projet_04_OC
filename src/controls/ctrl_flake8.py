from src.views import ShowPepHeight
import subprocess


class CtrlPepHeight:
    def __init__(self, view_main, os):
        self.subprocess = subprocess
        self.show_flake8 = ShowPepHeight
        self.list_answer_choice_show_flake = [1, 2]
        self.view_main = view_main
        self.os = os

    def control_pep_console(self):
        check = self.subprocess.run(
            'flake8 --exclude=env', shell=True)
        if check.returncode == 0:
            print(self.show_flake8.result_check_flake_no_errors())
        else:
            return check

    def control_pep_html(self):
        return self.subprocess.run(
            'flake8 --exclude=env --format=html --htmldir=flake_report',
            shell=True)

    def choice_show_flake(self):
        print(self.show_flake8.choice_flake8())
        answer = self.view_main.view_input.try_choice_input(
            self.list_answer_choice_show_flake)
        if answer == "1":
            self.control_pep_console()
        elif answer == "2":
            self.control_pep_html()
            if self.os.path.exists("../Projet_04_OC/flake_report/index.html"):
                print(self.show_flake8.result_true_pep_html())
            else:
                print(self.show_flake8.result_false_pep_html())
