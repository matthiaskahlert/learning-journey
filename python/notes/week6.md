# Meine Markdown notes Woche 6
## Grafische Benutzeroberflächen
GUI oder graphical user interface hat Bausteine namens Widgets (Window/Gadget). Ein Widget ist ein Objekt eines Typs, der aus dem Modul tkinter importiert wird.

### Widgets aus dem tkinter modul
| Widget | Erklärung
| Button | Schaltfläche
| Canvas | Rechteckige Fläche für Grafik
| Checkbutton | Quadratische Schaltfläche für m-aus-n-Auswahl
| Entry | Einzeiliges Eingabefeld
| Label | Rechteckige Fläche für einen Text oder ein Bild
| PhotoImage | Bild
| Radiobutton | Runde Schaltfläche für 1-aus-n-Auswahl
| Text | Mehrzeiliges Textfeld für die Eingabe und Ausgabe von Text (Texteditor)
| Tk | Anwendungsfenster|


Mit from tkinter import Tk, Label importierst du die benötigten Klassen für das Fenster und das Label.
Ein Fenster wird mit fenster = Tk() erstellt.
Ein Label wird mit Label(master=fenster, text='Guten morgen!') erzeugt und mit pack() im Fenster platziert.
Mit fenster.title('Hallo Welt!') wird der Fenstertitel gesetzt.
fenster.mainloop() startet die Ereignisschleife, damit das Fenster angezeigt wird und auf Eingaben reagiert. Ohne mainloop() würde das Fenster sofort wieder geschlossen.
Die Dateiendung .pyw sorgt dafür, dass das Skript ohne Konsolenfenster läuft (praktisch für GUI-Anwendungen).
pack() ist notwendig, damit das Label im Fenster sichtbar wird.

### Widgets gestalten

Widgets haben änderbare Eigenschaften. Folgende Optionen kann man auf fast alle Widgets anwenden: 
| Option         | Erklärung
| bd, borderwidth| Breite des sichtbaren Rands / Rahmens um das Widget
| bg, background | Hintergrundfarbe
| fg, foreground | Vordergrundfarbe (Textfarbe)
| font           | Font-Deskriptor für den verwendeten Schrifttyp, z.B. font=('Courier', 20)
| height         | Höhe des Widgets (senkrecht)
| image          | Name eines Bilds (Image-Objekt), das auf dem Widget zu sehen ist
| justify        | Ausrichtung von Textzeilen auf dem Widget: CENTER, LEFT, RIGHT.
| relief         | Form des Rahmens: SUNKEN, RAISED, GROOVE, RIDGE, FLAT
| text           | Beschriftung des Widgets
| width          | Breite des Widgets (waagerecht)|

### Wichtige Methoden für Widgets
| Methode | Erklärung |
| after (ms, func[, arg1[, ... ]]) | Aufruf einer Funktion oder Methode nach ms Millisekunden |
| bell() | Erzeugt Glockenklang. |
| cget(option) | Liefert den Wert der angegebenen Option. |
| config(option1=wert1, ... ) | Das Widget wird neu konfiguriert, die angegebenen Optionen erhalten neue Werte. Beispiel: label.config(text='Neu') |
| destroy() | Das Widget wird gelöscht. |
| grid( ... ) | Das Widget wird in das Raster-Layout des Master-Widgets (z.B. das Anwendungsfenster) eingefügt. |
| pack( ... ) | Das Widget wird nach dem Pack-Prinzip in das Layout des Master-Widgets (z.B. das Anwendungsfenster) eingefügt. |





