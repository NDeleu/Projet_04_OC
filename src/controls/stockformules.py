
"""
Créer ds le view une condition au contrôle du tps : soit :
    Bullet
    Blitz
    Coup Rapide
un des 3 pas autre chose
"""
"""
proposer input de description, exemple d'utilisation : tournoi1.description = "Yo je suis le président"
"""

class People:
    def __init__(self, name, age, score=0):
        self.name = name
        self.age = age
        self.score = score


list1 = []
list2 = []

for y in range(5):
    list1.append(People(input("name"), input("age")))
print(list1)

for el in list1:
    list2.append(el.__dict__)
print(list2)

for li in list2:
    for la in list1:
        if li == la.__dict__:
            list2[list2.index(li)] = la
print(list2)

