from random import randint
for i in range(5):
    zufallszahl = randint(1, 6)
    print(zufallszahl, end ='')


from random import choice
personen = ['Alex', 'Tina', 'Annelie', 'Tom']
person = choice(personen)
print(person, 'wurde zufallig gewählt.')