from src.views.exceptioninput import ExceptionInput, UnrecognizedInput, NotEnoughCharacters, NotExists, \
    TooManyCharacters, AlreadyExists
from src.views.showerrorinput import ShowErrorInput
import datetime


class CtrlViewInput:
    def __init__(self):
        self.exception_input = ExceptionInput()
        self.show_error_input = ShowErrorInput()

    def try_date_input(self):
        date_tried = input("Saisissez la date de naissance du joueur : ")
        try:
            return datetime.datetime.strptime(date_tried, "%Y-%m-%d").date()
        except ValueError:
            print(self.show_error_input.error_date_input())
            return self.try_date_input()

    def try_is_not_digit(self):
        answer = input("Saisissez le nombre désiré : ")
        try:
            return self.exception_input.except_is_not_digit(answer)
        except ValueError:
            print(self.show_error_input.error_value_num_input())
            return self.try_is_not_digit()

    def try_id_player_input(self):
        id_player_tried = input("Saisissez l'identifiant échec du joueur : ")
        try:
            return self.exception_input.except_invalid_format_id_player(id_player_tried)
        except NotEnoughCharacters:
            print(self.show_error_input.error_not_enough_characters(6))
            return self.try_id_player_input()
        except TooManyCharacters:
            print(self.show_error_input.error_too_many_characters(6))
            return self.try_id_player_input()
        except ValueError:
            print(self.show_error_input.error_id_player_input())
            return self.try_id_player_input()

    def try_alphanum_string_input(self, len_min=1, len_max=999):
        string_tried = input(f"Saisis : ")
        try:
            return self.exception_input.except_alphanum_min_max_characters(string_tried, len_min, len_max)
        except ValueError:
            print(self.show_error_input.error_value_alphanum_input())
            return self.try_string_input(len_min, len_max)
        except NotEnoughCharacters:
            print(self.show_error_input.error_not_enough_characters(len_min))
            return self.try_string_input(len_min, len_max)
        except TooManyCharacters:
            print(self.show_error_input.error_too_many_characters(len_max))
            return self.try_string_input(len_min, len_max)

    def try_string_input(self, len_min=1, len_max=999):
        string_tried = input(f"Saisis : ")
        try:
            return self.exception_input.except_min_max_characters(string_tried, len_min, len_max)
        except NotEnoughCharacters:
            print(self.show_error_input.error_not_enough_characters(len_min))
            return self.try_string_input(len_min, len_max)
        except TooManyCharacters:
            print(self.show_error_input.error_too_many_characters(len_max))
            return self.try_string_input(len_min, len_max)

    def try_not_exists(self, type_item, result_check):
        # recherche dans la base de donnée un element, renvoie vrai s'il ne s'y trouve pas, et leve l'exception
        seek_input = input(f"Saisis : ")
        try:
            return self.exception_input.except_not_exists(
                seek_input, result_check)
        except NotExists:
            print(self.show_error_input.error_not_exists(type_item, seek_input))
            return self.try_not_exists(type_item, result_check)

    def try_already_exists(self, type_item, input_given, result_check):
        # recherche dans la base de donnée un element, renvoie vrai s'il s'y trouve, et leve l'exception
        seek_input = input_given
        try:
            return self.exception_input.except_already_exists(
                seek_input, result_check)
        except AlreadyExists:
            print(self.show_error_input.error_already_exists(type_item, seek_input))
            return False

    def try_choice_input(self, list_given):
        choice_input = input("Saisissez le numéro correspondant à votre choix : ")
        try:
            return self.exception_input.except_unrecognized_input(choice_input, list_given)
        except ValueError:
            print(self.show_error_input.error_value_num_input())
            return self.try_choice_input(list_given)
        except UnrecognizedInput:
            print(self.show_error_input.error_choice_input())
            return self.try_choice_input(list_given)
