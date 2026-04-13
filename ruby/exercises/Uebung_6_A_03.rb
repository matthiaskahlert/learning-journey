# Entwickle eine Ruby-Anwendung, die eine Hierarchie von Klassen repräsentiert,
# die verschiedene Arten von Haustieren darstellen.
# Jede Klasse sollte mindestens eine Methode haben,
# die spezifisch für diese Art von Haustier ist.

# a) Erstelle eine Basisklasse "Haustier" mit einer Methode namens "füttern",
# die eine Ausgabe "Das Haustier wird gefüttert" erzeugt.

# b) Erstelle eine Unterklasse "Hund" und "Katze",
# die von der Basisklasse "Haustier" erben.
# Füge in jeder dieser Klassen eine Methode hinzu,
# die spezifisch für diese Art von Haustier ist.
# Zum Beispiel könnte die Klasse "Hund" eine Methode "bellen" haben,
# die die Ausgabe "Der Hund bellt" erzeugt,
# und die Klasse "Katze" könnte eine Methode "schnurren" haben,
# die die Ausgabe "Die Katze schnurrt" erzeugt.

# c) Demonstriere die Verwendung dieser Klassen und Methoden in deinem Code,
# indem du Instanzen von "Hund" und "Katze" erstellst
# und ihre spezifischen Methoden sowie die geerbte Methode "füttern" aufrufst.

# a) Basisklasse Haustier
class Haustier
  def fuettern
    puts 'Das Haustier wird gefüttert'
  end
end

# b) Unterklassen Hund und Katze
class Hund < Haustier
  def bellen
    puts 'Der Hund bellt'
  end
end

class Katze < Haustier
  def schnurren
    puts 'Die Katze schnurrt'
  end
end

# c) Demonstration

mein_hund = Hund.new
mein_hund.fuettern
mein_hund.bellen

meine_katze = Katze.new
meine_katze.fuettern
meine_katze.schnurren
