
class Player:
    def __init__(self, name, surname, age, classement):
        self.name = name
        self.surname = surname
        self.age = age
        self.classement = classement
        self.round_point = 0

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return str(self)