# trainer.py
import random, time
print('Multiplikationstrainer')
print('-'*30)
startzeit = time. time()
for i in range(5):
    a = random. randint (1,20)
    b = random. randint(1,10)
    ergebnis =- 1
    while ergebnis != a * b:
        prompt = f"{a} * {b} = "
        ergebnis = int(input(prompt))
        if ergebnis == a * b:
            print('Richtig!')
        else:
            print('Falsch!',
                  'Versuchen Sie es noch einmal!')

zeit = round(time.time() - startzeit)
print('Für die Aufgaben haben Sie',
zeit, 'Sekunden benötigt.')

