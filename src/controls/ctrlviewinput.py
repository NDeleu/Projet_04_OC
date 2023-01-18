from src.views.formatinput import FormatInput
from src.views.exceptioninput import ExceptionInput, UnrecognizedInput, NotEnoughCharacters, NotExists, \
    TooManyCharacters, InvalidFormat, AlreadyExists
from src.views.showerrorinput import ShowErrorInput


class CtrlViewInput:
    def __init__(self):
        self.format_input = FormatInput()
        self.exception_input = ExceptionInput()
        self.show_error_input = ShowErrorInput()

    def number_choice_input():
        return input("Votre choix : ")

    number_choice_input = staticmethod(number_choice_input)

    def try_input(self, len_min, len_max):
        try:
            print(self.exception_input.except_min_max_characters(self.number_choice_input(), len_min, len_max))
        except NotEnoughCharacters:
            print("not enough characters, please retry")
            self.try_input(len_min, len_max)
        except TooManyCharacters:
            print("too many characters, please retry")
            self.try_input(len_min, len_max)

