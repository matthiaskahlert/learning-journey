from time import time
import pickle

PFAD = 'python/exercises/Kapitel 8 Uebungen/plan.dat' # pfad wird als globale kostante gespeichert
MENÜ = '''
n: neue Aktivität eingeben
d: dringendste Aktivitaten
e: Ende des Programms
'''
def laden():
    try:
        with open(PFAD, 'rb') as f: # modus rb um binärdatei zum lesen zu öffnen
            plan = pickle.load(f)
    except: # falls datei nicht existiert, wirfd sie erstellt
        plan = []
    return plan

def speichern (plan):
    with open(PFAD, 'wb') as f: # modus wb um binärdatei zum schreiben zu öffnen
        pickle.dump(plan, f)

def eingabe(plan):
    aktivität = input('Aktivität: ')
    stunden = input('In wie viel Stunden zu erledigen (nur ganze std)? ')
    plan += [(int(stunden) * 3600 + time(), aktivität)]
    speichern(plan)

def ausgabe(plan):
    plan.sort() # sortiert nach deadline
    dringend = plan[0:2]
    for deadline, aktivität in dringend:
        restzeit = (deadline - time())/60
        print('Noch', round(restzeit), 'Minuten für:', aktivität)

plan = laden()
auswahl = 'x'
while auswahl != 'e':
    print (MENÜ)
    auswahl = input('Auswahl: ')
    if auswahl == 'n':
        eingabe(plan)
    elif auswahl == 'd':
        ausgabe(plan)
print('Bis bald!')
