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

pack() optionen:
| Option  | Erklärung                                                               | Mögliche Werte                        |
| anchor  | Positioniert das Widget in der Zelle nach Himmelsrichtung oder mittig.  | CENTER, E, N, NE, NW, S, SE, SW, W    |
| expand  | Ob das Widget beim Vergrößern des Fensters mitwächst.                   | 0 (nicht anpassen), 1 (anpassen)      |
| fill    | In welche Richtung das Widget den freien Raum ausfüllt.                 | X, Y, BOTH, None                      |
| padx    | Fügt rechts und links vom Widget Abstand in Pixeln hinzu.               | z.B. 10                               |
| pady    | Fügt oberhalb und unterhalb vom Widget Abstand in Pixeln hinzu.         | z.B. 10                               |
| side    | An welcher Seite des Masters das Widget angeordnet wird.                | LEFT, RIGHT, TOP, BOTTOM              |

### Rasterlayout (grid) in Tkinter

Mit dem grid-Layoutmanager kannst du Widgets in einem tabellenartigen Raster (Zeilen und Spalten) anordnen. Jedes Widget bekommt eine Position durch die Angabe von row (Zeile) und column (Spalte).
Du kannst Zellen mit rowspan und columnspan über mehrere Zeilen oder Spalten strecken.
Mit den Optionen sticky, padx, pady und ipadx, ipady kannst du die Ausrichtung und Abstände innerhalb der Zelle steuern.
Das Rasterlayout eignet sich besonders, wenn du komplexere, tabellenartige Anordnungen von Widgets brauchst

| Option      | Erklärung                                                                                                         |
|-------------|------------------------------------------------------------------------------------------------------------------|
| column      | Die Nummer der Spalte, in der das Widget eingetragen werden soll. Default ist 0.                                 |
| columnspan  | Das Widget erstreckt sich über n benachbarte Zellen in einer Zeile.                                              |
| padx        | Fügt rechts und links vom Widget in der angegebenen Länge leeren Raum hinzu (z.B. padx=10 für 10 Pixel Abstand). |
| pady        | Fügt oberhalb und unterhalb des Widgets leeren Raum hinzu.                                                       |
| row         | Die Nummer der Zeile, in der das Widget eingetragen werden soll. Default ist 0.                                  |
| rowspan     | Das Widget erstreckt sich über n Zellen in der gleichen Spalte.                                                  |

### Textwidgets (Tkinter)
1️⃣ Entry-Widget (einzeilig)

Für einzeilige Texteingabe

get() → liefert aktuellen Inhalt als String

Typisches EVA-Prinzip:

Eingabe: mathematischer Ausdruck im Entry
Verarbeitung: eval() wertet Ausdruck aus
Ausgabe: Ergebnis oder Fehlermeldung im Label

Ideal für kurze Eingaben (z. B. Formeln, Namen, Zahlen)

2️⃣ Text-Widget (mehrzeilig)

Für längere Texte
Frei einstellbar: width, height
Kann auch nur zur Ausgabe verwendet werden
Vorteil gegenüber Label: automatischer Zeilenumbruch

Wichtige Option:
wrap=WORD


→ Zeilenumbruch nach vollständigen Wörtern
(Standard: Zeichenumbruch)


3️⃣ Wichtige Methoden
Methode	Funktion
insert(index, text)	Text einfügen
get(index1[, index2])	Textbereich lesen
delete(index1[, index2])	Zeichen/Bereich löschen
| Methode                | Erklärung                                                                                                 |
|------------------------|----------------------------------------------------------------------------------------------------------|
| delete(index1[,index2])| Löscht das Zeichen an Position index1, oder den Bereich von index1 bis index2, wenn beide angegeben sind.|
| get(index1[,index2])   | Gibt den Text von index1 bis einschließlich index2 zurück. Ohne index2 nur das Zeichen an index1.        |
| insert(index, text)    | Fügt hinter der Position index den Text ein.                                                             |

4️⃣ Wichtige Index-Angaben
Zeile & Spalte

Format: 'zeile.spalte'
Zeilen starten bei 1
Spalten starten bei 0

Beispiele:

'1.0' → erstes Zeichen
'3.2' → 3. Zeichen in Zeile 3

Spezielle Indexe
Index	Bedeutung
END	letztes Zeichen im Text
'zeile.end'	letztes Zeichen einer Zeile
INSERT	aktuelle Cursorposition
Beispiele:
text.delete('1.0', END)      # kompletten Text löschen
text.get('1.0','1.end')      # erste Zeile auslesen
text.insert(INSERT,'Text')   # an Cursorposition einfügen

Merke

Entry = eine Zeile
Text = mehrere Zeilen + Editor-Funktionen
Text-Zugriff erfolgt immer über Indexe

### Radiobuttons

Jeder Radiobutton hat einen Wert (value), der bei Auswahl einer Kontrollvariablen zugewiesen wird.
Mit command=... kann ein Eventhandler (Funktion) beim Klick ausgeführt werden.
Mit select() kann ein Radiobutton vorselektiert werden.

Radiobuttons funktionieren immer nach diesem Muster:
```py
variable = StringVar()

Radiobutton(variable=variable, value='A')
Radiobutton(variable=variable, value='B')
Radiobutton(variable=variable, value='C')
```

Alle Buttons teilen sich eine gemeinsame Variable
Jeder Button hat einen eigenen value

variable.get() liefert den aktuell gewählten Wert

[Zur Währungsrechner Aufgabe](./python\exercises\Kapitel 11 Uebungen\währungsumrechner.pyw)

Währungsauswahl per Radiobutton, Eingabe in Entry, Umrechnung per Button.
Dictionary für Wechselkurse, Kontrollvariable für Währung, Ergebnis im Label.







### Dialogboxen
Mit tkinter.filedialog können Dateien geöffnet und gespeichert werden.
Dialogbox gibt Pfad oder Stream zurück, Textfeld kann damit befüllt werden.
Eine Dialogbox erscheint mitten auf dem Bildschirm und führt einen kleinen Dialog mit dem Benutzer. 
Das Untermodul tkinter.filedialog enthält Funktionen zur Erzeugung von Dialogboxen zum Laden und Speichern von Dateien.

| Funktion           | Erklärung                                                                                                                                         |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| askopenfile()      | Erzeugt eine Dialogbox zum Öffnen einer Datei. Gibt nach dem Dialog einen geöffneten Stream zurück.                                                |
| askopenfilename()  | Erzeugt eine Dialogbox zum Öffnen einer Datei. Gibt nach dem Dialog den Pfad zur ausgewählten Datei zurück. Mit open() kann die Datei geöffnet werden. Vorteil: Codierung (z.B. utf-8) kann gewählt werden. |
| asksaveasfile()    | Erzeugt eine Dialogbox zum Speichern einer Datei. Gibt nach dem Dialog einen geöffneten Stream zurück.                                             |

### Threads
Threads (Nebenläufigkeit)


GUI läuft normalerweise sequenziell (ein Thread).
Für parallele Abläufe (z.B. Countdown) kann eine Funktion mit _thread.start_new_thread() in einem eigenen Thread ausgeführt werden, damit die Oberfläche aktiv bleibt.
Standardmäßig läuft Python-Code sequenziell (eine Anweisung nach der anderen).
In GUIs ist oft Nebenläufigkeit nötig, z.B. für Animationen oder parallele Abläufe.
Parallele Abläufe werden mit sogenannten Threads realisiert, damit mehrere Dinge gleichzeitig passieren können (z.B. Fenster bedienen und Countdown anzeigen).

Layout:

Widgets werden mit pack() (nebeneinander/untereinander) oder grid() (Raster) angeordnet.
Optionen wie row, column, padx, pady, rowspan, columnspan steuern das Rasterlayout.


### Rückblick – Tkinter Grundlagen

Mit dem Modul tkinter lassen sich grafische Benutzeroberflächen (GUI – Graphical User Interface) in Python programmieren. GUI-Programme werden üblicherweise mit der Dateiendung .pyw gespeichert.

Eine GUI basiert auf einem Anwendungsfenster (Tk), in das verschiedene Widgets eingefügt werden. Diese Widgets übernehmen unterschiedliche Aufgaben:

Label dient zur Anzeige von Texten und Bildern.

Entry ermöglicht eine einzeilige Texteingabe.

Text wird für mehrzeilige Eingaben oder längere Ausgaben verwendet.

Radiobutton erlaubt die Auswahl zwischen mehreren Optionen.

Button löst beim Anklicken eine Funktion aus und startet damit eine Aktion.

Für die Anordnung der Widgets stehen verschiedene Layout-Methoden zur Verfügung:

pack() ordnet Widgets nebeneinander oder untereinander an.

grid() platziert Widgets in einem Raster aus Zeilen und Spalten.

Zusätzlich können über Dialogboxen Dateien geöffnet oder gespeichert werden. Durch den Einsatz von Threads lassen sich Funktionen im Hintergrund ausführen, sodass die Benutzeroberfläche weiterhin reaktionsfähig bleibt und nicht „einfriert“.

## Grafische programmierung - Bilder auf Schaltflächen und Labels

In tkinter können Widgets wie Label oder Button statt Text auch Bilder anzeigen. Dazu wird zunächst ein PhotoImage-Objekt erzeugt:

from tkinter import *

bild = PhotoImage(file="icon.png")
label = Label(master=fenster, image=bild)


Unterstützte Formate sind GIF, PNG, PPM und PGM. Andere Formate (z. B. JPG) funktionieren nicht direkt. Wichtig: Das PhotoImage-Objekt muss in einer Variable gespeichert bleiben, sonst wird es vom Garbage Collector entfernt.


### PhotoImage - Bilder pixelweise verändern

Ein PhotoImage kann pixelweise analysiert und verändert werden. Das ist möglich, aber bei größeren Bildern langsam.

| Methode                | Erklärung                                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| `get(x, y)`            | Farbwert des Pixels an Position `(x, y)` als `(R, G, B)`                                                     |
| `put(farbe, position)` | Setzt Pixel oder Rechteck auf Farbe (`'#rrggbb'` oder Name). `(x, y)` = Pixel, `(x1, y1, x2, y2)` = Rechteck |
| `width()`              | Breite des Bildes in Pixeln                                                                                  |
| `height()`             | Höhe des Bildes in Pixeln                                                                                    |
| `write(pfad)`          | Speichert Bild unter Pfad                                                                                    |


put() akzeptiert:

(x, y) → einzelnes Pixel

(x1, y1, x2, y2) → Rechteckbereich

Projekt: Graustufen-Umwandlung

Ein Farbfoto wird in ein Bild mit drei Helligkeitsstufen umgewandelt: Schwarz, Grau, Weiß.

Algorithmus:

Für jedes Pixel Helligkeit berechnen (sum(r, g, b)).

Zwei Schwellenwerte S1 und S2 definieren.

Einteilung:

< S1 → schwarz

< S2 → grau

sonst → weiß
```py
from tkinter import *

DATEINAME = "gesicht.png"
S1, S2 = 255, 510

def bearbeiten():
    for x in range(bild.width()):
        for y in range(bild.height()):
            c = bild.get(x, y)
            helligkeit = sum(c)
            if helligkeit < S1:
                bild.put("black", (x, y))
            elif helligkeit < S2:
                bild.put("grey", (x, y))
            else:
                bild.put("white", (x, y))

fenster = Tk()
bild = PhotoImage(file=DATEINAME)

label = Label(master=fenster, image=bild)
button = Button(master=fenster, text="Bearbeiten",
                font=("Arial", 14),
                command=bearbeiten)

label.pack()
button.pack(fill=X)
fenster.mainloop()
```

Hinweis: Die Verarbeitung ist langsam, da jedes Pixel einzeln bearbeitet wird. Deutlich schneller geht es mit NumPy, da Bilder mathematisch als Arrays betrachtet werden können.

### Canvas - digitale zeichenfläche

Ein Canvas ist eine Zeichenfläche, auf der grafische Objekte wie Linien, Rechtecke, Ovale oder Texte erzeugt, verschoben oder gelöscht werden können.
```py
from tkinter import *

fenster = Tk()
canvas = Canvas(master=fenster,
                width=200, height=200,
                bg="white")

canvas.create_oval(50, 50, 150, 150,
                   fill="blue",
                   outline="")

canvas.pack()
fenster.mainloop()
```

Hier wird ein weißer Canvas mit einem blauen Kreis erzeugt.

| Methode                            | Erklärung                              |
| ---------------------------------- | -------------------------------------- |
| `create_line(...)`                 | Linie aus mehreren Punkten             |
| `create_oval(x1, y1, x2, y2)`      | Ellipse in Bounding Box                |
| `create_rectangle(x1, y1, x2, y2)` | Rechteck                               |
| `create_text(x, y)`                | Textobjekt                             |
| `coords(id, ...)`                  | Koordinaten eines Objekts lesen/ändern |
| `move(id, dx, dy)`                 | Objekt verschieben                     |
| `delete(id)`                       | Objekt löschen                         |
| `find_all()`                       | IDs aller Objekte                      |
| `find_closest(x, y)`               | Nächstgelegenes Objekt                 |
| `find_overlapping(x1, y1, x2, y2)` | Objekte im Rechteckbereich             |

| Option    | Bedeutung                                         |
| --------- | ------------------------------------------------- |
| `fill`    | Füllfarbe (Standard: transparent)                 |
| `outline` | Randfarbe (Standard: schwarz, `""` = transparent) |
| `width`   | Linienstärke                                      |


### Linien zeichnen

Linien bestehen aus einer Folge von Punktkoordinaten:

canvas.create_line(0, 50, 100, 50, 200, 150)


Alternativ mit Liste:

punkte = [0, 100, 100, 50, 200, 150]
canvas.create_line(punkte)

| Option   | Bedeutung                                         |
| -------- | ------------------------------------------------- |
| `fill`   | Linienfarbe                                       |
| `width`  | Linienstärke                                      |
| `smooth` | True = Parabolischer Spline statt gerade Segmente |

### Zusammenfassung

PhotoImage ermöglicht Bildanzeige in Labels und Buttons.

Pixelweise Bearbeitung ist möglich, aber langsam.

Graustufen-Transformation basiert auf Helligkeitsschwellen.

Canvas ist eine flexible Zeichenfläche für grafische Objekte.

Grafische Elemente werden über create_...() erzeugt und über IDs verwaltet.

Gestaltung erfolgt über Optionen wie fill, outline, width oder smooth.

Damit bildet dieses Kapitel die Grundlage für einfache Bildverarbeitung und interaktive 2D-Grafik in tkinter.

