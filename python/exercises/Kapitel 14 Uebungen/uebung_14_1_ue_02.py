""" 
Entwickle eine Python-Klasse namens Buch, die zur Verwaltung einer kleinen Bibliothek dient. 
Die Klasse soll folgende Attribute und Methoden haben:

a) Die Klasse soll drei Attribute haben: 
titel (String), 
autor (String) und 
ausgeliehen (Boolean), wobei ausgeliehen standardmäßig auf False gesetzt ist.

b) Schreibe eine Initialisierungsmethode __init__, die titel und autor als Parameter erhält 
und diese zusammen mit dem Standardwert für ausgeliehen setzt.

c) Füge eine Methode ausleihen hinzu, die das Attribut ausgeliehen auf True setzt, 
falls das Buch nicht bereits ausgeliehen ist. 
Falls das Buch bereits ausgeliehen ist, soll eine Nachricht "Buch bereits ausgeliehen" ausgegeben werden.

d) Füge eine Methode zurueckgeben hinzu, die das Attribut ausgeliehen auf False setzt, 
falls das Buch ausgeliehen war. 
Falls das Buch nicht ausgeliehen ist, soll eine Nachricht "Buch war nicht ausgeliehen" ausgegeben werden.

e) Schreibe eine Methode status, die 
den Titel, 
Autor und 
den Ausleihstatus des Buches in einem Satz ausgibt. 
 """

# Klasse definieren
class Buch:
    """Die Buch Klasse zur Verwaltung einer kleinen Bibliothek"""
    def __init__(self, titel, autor):
        """Initialisierungsmethode, die titel und autor als Parameter enthält"""
        self.titel = titel
        self.autor = autor
        self.ausgeliehen = False
    
    def ausleihen(self):
        """Setzt das Attribut ausgeliehen auf True, falls das Buch nicht bereits ausgeliehen ist."""
        if not self.ausgeliehen:
            self.ausgeliehen = True
        else:
            print("Das Buch ist bereits ausgeliehen")
    
    def zurückgeben(self):
        """Setzt das Attribut ausgeliehen auf False, falls das Buch ausgeliehen war."""
        if self.ausgeliehen:
            self.ausgeliehen = False
        else:
            print("Das Buch war nicht ausgeliehen")
    
    def status(self):
        """Gibt den Titel, Autor und den Ausleihstatus des Buches in einem Satz aus."""
        if self.ausgeliehen:
            ausleihstatus = "ausgeliehen"
        else:
            ausleihstatus = "verfügbar"
            return f'"{self.titel}" von {self.autor} ist aktuell {ausleihstatus}.'
        
    # Verwendung der Klasse
if __name__ == "__main__":
    buch1 = Buch("Der Alchimist", "Paulo Coelho")
    buch2 = Buch("1984", "George Orwell")

    print(buch1.status())
    print(buch2.status())

    buch1.ausleihen()
    print(buch1.status())

    buch1.ausleihen()  # Versuch, das Buch erneut auszuleihen

    buch1.zurückgeben()
    print(buch1.status())

    buch1.zurückgeben()  # Versuch, das Buch zurückzugeben, wenn es nicht ausgeliehen ist