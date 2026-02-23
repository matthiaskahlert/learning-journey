""" 
Aufgabe: Objektorientierte Programmierung

Entwickle ein Python-Programm, das ein einfaches Bankkonto-Management-System simuliert. Das Programm soll folgende Funktionalitäten umfassen:

a) Definiere eine Klasse Bankkonto, die Attribute für den Kontoinhaber (inhaber), die Kontonummer (konto_nr), den aktuellen Kontostand (kontostand) und eine Liste der letzten zehn Transaktionen (transaktionen) enthält. Der Kontostand soll mit einem Anfangswert von 0 initialisiert werden, und die Liste der Transaktionen soll leer sein.

b) Implementiere eine Methode einzahlen, die einen Betrag annimmt und den Kontostand entsprechend erhöht. Die Methode soll außerdem die Transaktion (Datum, Uhrzeit, Betrag) in der Transaktionsliste speichern. Verwende das Modul datetime, um das aktuelle Datum und die Uhrzeit zu erfassen.

c) Implementiere eine Methode abheben, die einen Betrag annimmt und prüft, ob der Betrag vom aktuellen Kontostand abgehoben werden kann. Wenn ja, soll der Betrag abgehoben und die Transaktion gespeichert werden. Wenn nicht, soll eine Ausnahme mit der Nachricht "Nicht genügend Guthaben" geworfen werden.

d) Füge eine Methode letzte_transaktionen hinzu, die die letzten zehn Transaktionen anzeigt.

e) Erstelle eine Instanz der Klasse Bankkonto für einen Benutzer und führe verschiedene Einzahlungen und Abhebungen durch. Verwende Ausnahmen, um Fehler wie das Abheben eines Betrags, der den Kontostand übersteigt, zu behandeln.

f) Implementiere eine einfache Benutzeroberfläche in der Konsole, die es dem Benutzer ermöglicht, Einzahlungen und Abhebungen zu tätigen und die letzten Transaktionen einzusehen. 
 """

import datetime


class Bankkonto:
    def __init__(self, inhaber, konto_nr):
        self.inhaber = inhaber
        self.konto_nr = konto_nr
        self.kontostand = 0
        self.transaktionen = []


    def einzahlen(self, betrag):
        self.kontostand += betrag
        self.transaktionen.append((datetime.datetime.now(), "Einzahlung", betrag))
        self.transaktionen = self.transaktionen[-10:]  # Behalte nur die letzten 10 Transaktionen


    def abheben(self, betrag):
        if self.kontostand >= betrag:
            self.kontostand -= betrag
            self.transaktionen.append((datetime.datetime.now(), "Abhebung", betrag))
            self.transaktionen = self.transaktionen[-10:]
        else:
            raise ValueError("Nicht genügend Guthaben")


    def letzte_transaktionen(self):
        for datum, typ, betrag in self.transaktionen:
            print(f"{datum}: {typ} von {betrag}€")


def main():
    konto = Bankkonto("Max Mustermann", "DE1234567890")
    while True:
        aktion = input("Wählen Sie eine Aktion: (E)inzahlen, (A)bheben, (T)ransaktionen anzeigen, (B)eenden: ").upper()
        if aktion == "E":
            betrag = float(input("Betrag zum Einzahlen: "))
            konto.einzahlen(betrag)
            print(f"{betrag}€ wurden eingezahlt.")
        elif aktion == "A":
            betrag = float(input("Betrag zum Abheben: "))
            try:
                konto.abheben(betrag)
                print(f"{betrag}€ wurden abgehoben.")
            except ValueError as e:
                print(e)
        elif aktion == "T":
            konto.letzte_transaktionen()
        elif aktion == "B":
            break
        else:
            print("Ungültige Aktion.")


if __name__ == "__main__":
    main()


