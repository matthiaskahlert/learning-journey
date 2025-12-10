""" Schreibe ein interaktives Programm, das die Kosten für eine Gruppenreise mit
einem Bus berechnet. Vom Benutzer werden folgende Angaben erfragt:
• Kosten für den Reisebus
• Hotelkosten pro Person
• Kosten für einen Reiseführer oder eine Reiseführerin
• Anzahl der Teilnehmer und Teilnehmerinnen
Ausgegeben werden:
• Die Gesamtkosten der Fahrt
• Der Betrag, den jeder Teilnehmer und jede Teilnehmerin zahlen muss
Möglicher Programmlauf:
Übung 3: Welches Volumen hat das Haus?
Schreibe ein interaktives Programm, das das Volumen eines Hauses mit
Satteldach berechnet. Beachte die Abbildung 3.14.
 """
# Autor: mkahlert
# Letzte Änderung: 10.12.25
print('Berechnung der Reisekosten für eine Gruppenreise mit dem Bus')
# Eingabe der Kosten und Teilnehmeranzahl
try:
    bus_kosten = float(input('Gib die Kosten für den Reisebus ein: '))
    hotel_kosten_pro_person = float(
        input('Gib die Hotelkosten pro Person ein: '))
    reisefuehrer_kosten = float(
        input('Gib die Kosten für den Reiseführer/die Reiseführerin ein: '))
    anzahl_teilnehmer = int(
        input('Gib die Anzahl der Teilnehmer und Teilnehmerinnen ein: '))
except ValueError:
    print("Fehlerhafte Eingabe: Bitte gültige Zahlen eingeben.")
    exit()  # Programm beenden
if anzahl_teilnehmer <= 0:
    print("Fehlerhafte Eingabe: Die Anzahl der Teilnehmer muss größer als 0 sein.")
    exit()  # Programm beenden
# Verarbeitung: Berechnung der Gesamtkosten und Kosten pro Teilnehmer
gesamt_kosten = bus_kosten + \
    (hotel_kosten_pro_person * anzahl_teilnehmer) + reisefuehrer_kosten
kosten_pro_teilnehmer = gesamt_kosten / anzahl_teilnehmer
# Ausgabe der Ergebnisse
gesamt_kosten = round(gesamt_kosten, 2)
kosten_pro_teilnehmer = round(kosten_pro_teilnehmer, 2)
print(f'Die Gesamtkosten der Fahrt betragen: {gesamt_kosten} Euro.')
print(
    f'Der Betrag, den jeder Teilnehmer zahlen muss: {kosten_pro_teilnehmer} Euro.')
