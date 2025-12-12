planeten = {'Merkur', 'Venus', 'Erde', 'Mars',
            'Jupiter', 'Saturn', 'Uranus', 'Neptun'}
print('Zähle alle Planeten unseres Sonnensystems auf!')
while planeten != set():
    eingabe = input('Planet: ')
    if eingabe in planeten:
        planeten = planeten - {eingabe}
        print('Richtig!')
    else:
        print('Sorry!', eingabe, 'hatten wir schon oder',
              eingabe, 'ist kein Planet')
print('Gluckwunsch. Du hast alle Planeten aufgezählt.')
