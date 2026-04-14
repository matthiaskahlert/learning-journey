# Du arbeitest an einem Ruby-Projekt, in dem du Daten aus einer Textdatei lesen und diese Daten verarbeiten musst. Die Textdatei enthält Informationen über verschiedene Personen in folgendem Format: Name, Beruf, Geschlecht, Alter. Jede Person ist in einer separaten Zeile aufgeführt.

# a) Beschreibe, wie du die Datei in Ruby öffnen und jede Zeile einzeln lesen würdest.

# b) Erkläre, wie du das "each"-Verfahren verwenden würdest, um jede Zeile der Datei zu lesen und die Informationen jeder Person zu extrahieren.

# c) Beschreibe, wie du die "gets"-Methode verwenden würdest, um eine bestimmte Anzahl von Zeilen aus der Datei zu lesen.

# d) Erkläre, wie du die "readlines"-Methode verwenden würdest, um alle Zeilen der Datei in ein Array zu lesen.

# e) Beschreibe, wie du die "read"-Methode verwenden würdest, um eine bestimmte Anzahl von Bytes aus der Datei zu lesen.

# a) Um eine Datei in Ruby zu öffnen und jede Zeile einzeln zu lesen, nutzt man File.open und kombiniert das mit each oder each_line.
# Das öffnet die Datei und geht Zeile für Zeile durch, sodass du jede Zeile direkt verarbeiten kannst.
# Beispiel:
File.open('personen.txt', 'r') do |file|
  file.each_line do |zeile|
    puts zeile
  end
end


# b) Das "each"-Verfahren ist ein Iterator, der jede Zeile der Datei nacheinander durchläuft.
# So kannst du z.B. jede Zeile aufteilen und die einzelnen Informationen herausziehen:
File.open('personen.txt', 'r') do |file|
  file.each do |zeile|
    name, beruf, geschlecht, alter = zeile.chomp.split(', ')
    puts "Name: #{name}, Beruf: #{beruf}, Geschlecht: #{geschlecht}, Alter: #{alter}"
  end
end


# c) Mit "gets" liest du jeweils die nächste Zeile aus der Datei. Möchtest du z.B. die ersten drei Zeilen lesen, kannst du das so machen:
File.open('personen.txt', 'r') do |file|
  3.times do
    zeile = file.gets
    puts zeile unless zeile.nil?
  end
end


# d) Mit "readlines" liest du alle Zeilen der Datei auf einmal und bekommst sie als Array zurück.
# Jede Zeile ist dann ein Element im Array:
zeilen = File.readlines('personen.txt')
puts zeilen.inspect


# e) Mit "read" kannst du eine bestimmte Anzahl von Bytes aus der Datei lesen, z.B. die ersten 20 Bytes:
File.open('personen.txt', 'r') do |file|
  inhalt = file.read(20)
  puts inhalt
end
