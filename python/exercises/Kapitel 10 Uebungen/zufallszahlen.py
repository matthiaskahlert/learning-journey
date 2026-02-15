# zufallszahlen.py
import sys, random
original_stdout = sys.stdout
with open('python\exercises\Kapitel 10 Uebungen\zahlen.txt', 'w') as sys.stdout:
    print('Zufallszahlen zwischen 1 und 1000')
    for i in range(5):
        print(i, random.randint(1, 1000)) # Alles, was jetzt mit print() ausgegeben wird, landet in der Datei zahlen.txt.
sys.stdout = original_stdout # sys.stdout wird wieder zurückgesetzt, sodass Ausgaben wieder auf dem Bildschirm erscheinen.
print('Zufallszahlen wurden in eine Datei geschrieben.') #
