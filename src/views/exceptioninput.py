

class ExceptionInput:
    def __init__(self):
        self.unrecognized_input = UnrecognizedInput()
        self.not_enough_characters = NotEnoughCharacters()
        self.too_many_characters = TooManyCharacters()
        self.not_exists = NotExists()
        self.already_exists = AlreadyExists()
        self.invalid_format = InvalidFormat()

    def except_unrecognized_input(self, answer, list_given):
        if answer not in list_given:
            raise self.unrecognized_input
        return answer

    def except_min_max_characters(self, answer, len_min=1, len_max=999):
        if len(answer) < len_min:
            raise self.not_enough_characters
        elif len(answer) > len_max:
            raise self.too_many_characters
        return answer

    def except_not_enough_characters(self, answer, len_min=1):
        if len(answer) < len_min:
            raise self.not_enough_characters
        return answer

    def except_too_many_characters(self, answer, len_max=999):
        if len(answer) > len_max:
            raise self.too_many_characters
        return answer

    def except_not_exists(self, answer, result_check):
        if result_check:
            raise self.not_exists
        return answer

    def except_already_exists(self, answer, result_check):
        if result_check:
            raise self.already_exists
        return answer

    def except_invalid_format_date(self):
        pass

    def except_invalid_format_id_player(self):
        pass

    def except_alphanumeric(self):
        pass

    def except_numeric(self):
        pass


class UnrecognizedInput(Exception):
    # pas dans la liste des entrées possibles
    pass


class NotEnoughCharacters(Exception):
    # pas assez de caractères
    pass


class TooManyCharacters(Exception):
    # trop de caractères
    pass


class InvalidFormat(Exception):
    # ne correspond pas au format attendu
    pass


class AlreadyExists(Exception):
    # l 'element existe deja
    pass


class NotExists(Exception):
    # l 'element n 'existe pas
    pass
