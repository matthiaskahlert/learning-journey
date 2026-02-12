from random import choice

STORY = '''In der Dämmerung betrat {held} mit seinem {artefakt} das geheimnisvolle {ort}.
Die Schatten flüsterten: "Nur mit dem {artefakt} kann {held} das uralte Rätsel lösen."
Plötzlich tauchte {gegner} auf und versperrte den Weg.
Doch {held} wusste: Mit Mut und dem {artefakt} kann er jede Gefahr überwinden.
Das Abenteuer beginnt...'''

ORTE = ['Drachenwald', 'Kristallhöhle', 'Magierturm', 'Verlorene Ruinen', 'Schattenmoor', 'Feuerberg']
GEGNER = ['ein finsterer Hexer', 'ein wütender Troll', 'eine listige Diebin', 'ein uralter Drache', 'ein Schattengeist']
held = input("Name des männlichen Helden: ")
artefakt = input("Name des Magischen Artefakts: ")
gegner = choice(GEGNER)
ort = choice(ORTE)
story = STORY.format(held=held, artefakt=artefakt, ort=ort, gegner=gegner)

print(story)