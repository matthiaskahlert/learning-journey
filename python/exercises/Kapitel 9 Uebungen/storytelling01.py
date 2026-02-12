# storytelling_1.py
from random import choice
STORY = '''Am Morgen ging {sie} mit ihrem {gegenstand} über
den {ort}. "Ach", dachte {sie}, "wie gut,
dass ich den {gegenstand} dabeihabe. Ohne {gegenstand} käme
ich mir irgendwie unvollstandig vor." '''
ORTE = ['Prinzipalmarkt', 'Domplatz']
sie = input("Weiblicher Vorname: ")
gegenstand = input("Gegenstand (männlich): ")
story = STORY. format(sie=sie, gegenstand=gegenstand, ort=choice(ORTE))

print(story)