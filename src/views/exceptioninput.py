

class ExceptionInput:
    def __init__(self):
        self.unrecognized_input = UnrecognizedInput()
        self.not_enough_characters = NotEnoughCharacters()
        self.too_many_characters = TooManyCharacters()
        self.not_exists = NotExists()
        self.already_exists = AlreadyExists()

    def except_unrecognized_input(self, answer, list_given):
        if not answer.isdigit():
            raise ValueError
        elif int(answer) not in list_given:
            raise self.unrecognized_input
        return answer

    def except_alphanum_min_max_characters(self, answer, len_min=1, len_max=999):
        if not answer.isalnum():
            raise ValueError
        elif len(answer) < len_min:
            raise self.not_enough_characters
        elif len(answer) > len_max:
            raise self.too_many_characters
        return answer

    def except_not_exists(self, answer, result_check):
        if result_check:
            raise self.not_exists
        return answer

    def except_already_exists(self, answer, result_check, len_min=1, len_max=999):
        if len(answer) < len_min:
            raise self.not_enough_characters
        elif len(answer) > len_max:
            raise self.too_many_characters
        elif result_check:
            raise self.already_exists
        return answer

    def except_invalid_format_id_player(self, answer):
        if len(answer) < 6:
            raise self.not_enough_characters
        elif len(answer) > 6:
            raise self.too_many_characters
        elif not answer[0:2].isdigit():
            raise ValueError
        elif not answer[2:6].isalpha():
            raise ValueError
        return answer


class UnrecognizedInput(Exception):
    # pas dans la liste des entrées possibles
    pass


class NotEnoughCharacters(Exception):
    # pas assez de caractères
    pass


class TooManyCharacters(Exception):
    # trop de caractères
    pass


class AlreadyExists(Exception):
    # l 'element existe deja
    pass


class NotExists(Exception):
    # l 'element n 'existe pas
    pass
