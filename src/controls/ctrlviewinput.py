from src.views.formatinput import FormatInput
from src.views.exceptioninput import ExceptionInput, UnrecognizedInput, NotEnoughCharacters, NotExists, \
    TooManyCharacters, AlreadyExists
from src.views.showerrorinput import ShowErrorInput
import datetime


class CtrlViewInput:
    def __init__(self):
        self.format_input = FormatInput()
        self.exception_input = ExceptionInput()
        self.show_error_input = ShowErrorInput()

    def try_date_input(self):
        date_tried = input("Saisissez la date de naissance du joueur : ")
        try:
            return datetime.datetime.strptime(date_tried, "%Y-%m-%d").date()
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD, please retry")
            return self.try_date_input()

    def try_id_player_input(self):
        id_player_tried = input("Saisissez l'identifiant échec du joueur : ")
        try:
            return self.exception_input.except_invalid_format_id_player(id_player_tried)
        except NotEnoughCharacters:
            print("not enough characters, please retry")
            return self.try_id_player_input()
        except TooManyCharacters:
            print("too many characters, please retry")
            return self.try_id_player_input()
        except ValueError:
            print("Incorrect data format, should be integer for first two characters, then alpha for next")
            return self.try_id_player_input()

    def try_string_input(self, setup_input="l'information attendue", len_min=1, len_max=999):
        string_tried = input(f"Saisissez {setup_input} : ")
        try:
            return self.exception_input.except_alphanum_min_max_characters(string_tried, len_min, len_max)
        except ValueError:
            print("Incorrect data forme, should be alphanumeric (a-z)(0-9)")
            return self.try_string_input(setup_input, len_min, len_max)
        except NotEnoughCharacters:
            print("not enough characters, please retry")
            return self.try_string_input(setup_input, len_min, len_max)
        except TooManyCharacters:
            print("too many characters, please retry")
            return self.try_string_input(setup_input, len_min, len_max)

    def try_not_exists(self, setup_input="l'information attendue"):
        # recherche dans la base de donnée un element, renvoie vrai s'il ne s'y trouve pas, et leve l'exception
        seek_input = input(f"Saisissez {setup_input} : ")
        try:
            """
            return self.exception_input.except_not_exists(
            seek_input, recherchedansbasededonneedansmanager(seek_input))
            """
            pass
        except NotExists:
            print("Input element not exists, please retry")
            return self.try_not_exists()

    def try_already_exists(self, setup_input="l'information attendue"):
        # recherche dans la base de donnée un element, renvoie vrai s'il s'y trouve, et leve l'exception
        seek_input = input(f"Saisissez {setup_input} : ")
        try:
            """
            return self.exception_input.except_already_exists(
            seek_input, recherchedansbasededonneedansmanager(seek_input))
            """
            pass
        except AlreadyExists:
            print("Input element already exists, please retry")
            return self.try_not_exists()

    def try_choice_input(self, list_given):
        choice_input = input("Saisissez le numéro correspondant à votre choix : ")
        try:
            return self.exception_input.except_unrecognized_input(choice_input, list_given)
        except ValueError:
            print("Incorrect data forme, should be numeric (0-9)")
            return self.try_choice_input(list_given)
        except UnrecognizedInput:
            print("Input enter not registered, please retry")
            return self.try_choice_input(list_given)
