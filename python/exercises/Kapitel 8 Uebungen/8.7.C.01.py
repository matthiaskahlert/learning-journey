""" 
Du arbeitest als Entwickler in einem Unternehmen, das eine Software zur Verwaltung von Kundenkontakten entwickelt. 
Deine Aufgabe ist es, ein Python-Modul zu erstellen, das folgende Funktionalitäten umfasst:

a) Erstelle eine Funktion speichere_kontakt, die als Parameter die Daten eines Kontakts (Name, E-Mail, Telefonnummer) entgegennimmt 
und diese in einer JSON-Datei speichert. Verwende dabei das JSON-Format. 
Achte darauf, dass bei jedem Aufruf der Funktion ein neuer Kontakt zur Datei hinzugefügt wird, 
ohne die bestehenden Daten zu überschreiben.

b) Implementiere eine Funktion lade_kontakte, die die gespeicherten Kontaktdaten aus der JSON-Datei liest 
und als Liste von Dictionaries zurückgibt. Jedes Dictionary in der Liste soll die Daten eines Kontakts repräsentieren.

c) Erstelle eine Fehlerbehandlung für beide Funktionen, um sicherzustellen, 
dass das Programm nicht abstürzt, falls die Datei nicht existiert oder beschädigt ist. 
Gib in solchen Fällen eine entsprechende Fehlermeldung aus.

d) Schreibe eine einfache Benutzeroberfläche (CLI), über die ein Benutzer neue Kontakte hinzufügen 
und die gespeicherten Kontakte anzeigen lassen kann. 
Verwende dazu die Funktionen speichere_kontakt und lade_kontakte. """
