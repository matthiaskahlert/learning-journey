# Aufgabe: Input / Output
# Du arbeitest an einem Projekt, bei dem du eine große Menge an Textdaten verarbeiten musst. Die Daten sind in einer Textdatei gespeichert, wobei jede Zeile eine separate Einheit darstellt. Deine Aufgabe ist es, ein Ruby-Skript zu erstellen, das folgende Aufgaben erfüllt:

# a) Lies die Textdatei Zeile für Zeile ein und gib jede Zeile auf der Konsole aus.
# b) Zähle die Anzahl der Zeilen in der Datei und gib diese Zahl aus.
# c) Erstelle eine neue Datei, in der jede Zeile der ursprünglichen Datei rückwärts geschrieben ist.
# d) Erstelle eine weitere Datei, in der die Zeilen der ursprünglichen Datei in zufälliger Reihenfolge angeordnet sind.

require 'securerandom'

# Funktion, um die Datei Zeile für Zeile zu lesen und auszugeben
def read_and_print_file(file_path)
  line_count = 0
  File.foreach(file_path) do |line|
    puts line
    line_count += 1
  end
  line_count
end

# Funktion, um eine Datei mit rückwärts geschriebenen Zeilen zu erstellen
def create_reversed_file(input_file, output_file)
  File.open(output_file, 'w') do |file|
    File.foreach(input_file) do |line|
      file.puts line.chomp.reverse
    end
  end
end

# Funktion, um eine Datei mit zufällig angeordneten Zeilen zu erstellen
def create_shuffled_file(input_file, output_file)
  lines = File.readlines(input_file)
  shuffled_lines = lines.shuffle(random: SecureRandom)
  File.open(output_file, 'w') do |file|
    shuffled_lines.each { |line| file.puts line }
  end
end

# Hauptprogramm
puts 'Bitte geben Sie den Pfad zur Eingabedatei ein:'
input_file = gets.chomp

if File.exist?(input_file)
  # a) Datei Zeile für Zeile lesen und ausgeben
  puts "\nInhalt der Datei:"
  line_count = read_and_print_file(input_file)

  # b) Anzahl der Zeilen ausgeben
  puts "\nAnzahl der Zeilen: #{line_count}"

  # c) Datei mit rückwärts geschriebenen Zeilen erstellen
  reversed_file = 'reversed_file.txt'
  create_reversed_file(input_file, reversed_file)
  puts "\nDatei mit rückwärts geschriebenen Zeilen wurde erstellt: #{reversed_file}"

  # d) Datei mit zufällig angeordneten Zeilen erstellen
  shuffled_file = 'shuffled_file.txt'
  create_shuffled_file(input_file, shuffled_file)
  puts "\nDatei mit zufällig angeordneten Zeilen wurde erstellt: #{shuffled_file}"
else
  puts 'Die angegebene Datei existiert nicht. Bitte überprüfen Sie den Pfad und versuchen Sie es erneut.'
end
