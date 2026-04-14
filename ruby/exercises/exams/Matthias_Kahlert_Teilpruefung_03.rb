# Du bist ein Softwareentwickler in einem Unternehmen, das eine Software für eine Bibliothek entwickelt. Deine Aufgabe ist es, ein Ruby-Programm zu erstellen, das die folgenden Anforderungen erfüllt:

# a) Erstelle eine Klasse namens "Buch". Diese Klasse sollte Eigenschaften wie "Titel", "Autor", "ISBN" und "Verfügbarkeit" haben.

# b) Erstelle eine Methode in der Klasse "Buch", die den Status der Verfügbarkeit ändert.

# c) Erstelle eine verschachtelte Klasse innerhalb der Klasse "Buch" namens "Ausleiher". Diese Klasse sollte Eigenschaften wie "Name" und "Mitgliedsnummer" haben.

# d) Erstelle eine Methode in der Klasse "Ausleiher", die es ermöglicht, ein Buch auszuleihen. Beim Ausleihen eines Buches sollte die Verfügbarkeit des Buches geändert werden.

# e) Erstelle eine Exception für den Fall, dass ein Buch, das bereits ausgeliehen ist, erneut ausgeliehen werden soll.

# f) Erstelle eine "if-elseif"-Struktur, um zu prüfen, ob ein Buch verfügbar ist oder nicht.

# g) Erstelle ein Array von Büchern und verwende "ranges", um bestimmte Bücher aus dem Array auszuwählen.

# a) Klasse Buch mit Eigenschaften
class Buch
  attr_accessor :titel, :autor, :isbn, :verfuegbar

  def initialize(titel, autor, isbn, verfuegbar = true)
    @titel = titel
    @autor = autor
    @isbn = isbn
    @verfuegbar = verfuegbar
  end

  # b) Methode in der Klasse "Buch", die den Status der Verfügbarkeit ändert.
  def ausleihen
    raise BuchBereitsAusgeliehenError, "Das Buch '#{@titel}' ist bereits ausgeliehen!" unless @verfuegbar

    @verfuegbar = false
  end

  def zurueckgeben
    raise "Das Buch '#{@titel}' ist bereits verfügbar!" if @verfuegbar

    @verfuegbar = true
  end

  # c) Verschachtelte Klasse Ausleiher
  class Ausleiher
    attr_accessor :name, :mitgliedsnummer

    def initialize(name, mitgliedsnummer)
      @name = name
      @mitgliedsnummer = mitgliedsnummer
    end

    # d) Methode zum Ausleihen eines Buches
    def buch_ausleihen(buch)
      buch.ausleihen # Verfügbarkeit wird in Buch#ausleihen geändert
      puts "#{@name} hat das Buch '#{buch.titel}' ausgeliehen."
    end

    # Methode zum Zurückgeben eines Buches
    def buch_zurueckgeben(buch)
      buch.zurueckgeben
      puts "#{@name} hat das Buch '#{buch.titel}' zurückgegeben."
    end
  end
end

# e) Exception für bereits ausgeliehenes Buch
class BuchBereitsAusgeliehenError < StandardError; end

# f) if-elsif-Struktur zur Prüfung der Verfügbarkeit (laut Aufgabenstellung)
def pruefe_verfuegbarkeit(buch)
  if buch.verfuegbar
    puts "Das Buch '#{buch.titel}' ist verfügbar."
  elsif !buch.verfuegbar
    puts "Das Buch '#{buch.titel}' ist ausgeliehen."
  end
end

# Hinweis: Ohne die Aufgabenstellung würde ich hier eher einen Ternary Operator verwenden:
# def pruefe_verfuegbarkeit(buch)
#   puts buch.verfuegbar ? "Das Buch '#{buch.titel}' ist verfügbar." : "Das Buch '#{buch.titel}' ist ausgeliehen."
# end

# g) Array von Büchern und Auswahl mit Range
buecher = [
  Buch.new('Der Hobbit', 'J.R.R. Tolkien', '978-3-123456-78-9'),
  Buch.new('1984', 'George Orwell', '978-3-987654-32-1'),
  Buch.new('Momo', 'Michael Ende', '978-3-555555-55-5'),
  Buch.new('Die Verwandlung', 'Franz Kafka', '978-3-111111-11-1'),
  Buch.new('Faust', 'Goethe', '978-3-222222-22-2')
]

# Auswahl der ersten drei Bücher mit Range (0..2)
puts 'Ausgewählte Bücher (Range 0..2):'
buecher[0..2].each { |buch| puts "- #{buch.titel} von #{buch.autor}" }

# Auswahl der letzten zwei Bücher mit Range (-2..-1)
puts 'Letzte zwei Bücher (Range -2..-1):'
buecher[-2..-1].each { |buch| puts "- #{buch.titel} von #{buch.autor}" }

# Testfälle
buch1 = buecher[0]
ausleiher = Buch::Ausleiher.new('Max Mustermann', 12_345)

pruefe_verfuegbarkeit(buch1)
ausleiher.buch_ausleihen(buch1)
pruefe_verfuegbarkeit(buch1)

# Versuch, ein bereits ausgeliehenes Buch erneut auszuleihen
begin
  ausleiher.buch_ausleihen(buch1)
rescue BuchBereitsAusgeliehenError => e
  puts e.message
end

# Buch zurückgeben
ausleiher.buch_zurueckgeben(buch1)
pruefe_verfuegbarkeit(buch1)

# Testroutinen mit Minitest
# require 'minitest/autorun'

# class BuchTest < Minitest::Test
#   def setup
#     # Wird vor jedem Test neu ausgeführt – frisches Buch-Objekt
#     @buch = Buch.new('Test Buch', 'Test Autor', '000-0-000000-00-0')
#     @ausleiher = Buch::Ausleiher.new('Test User', 99_999)
#   end

#   def test_buch_ist_zu_beginn_verfuegbar
#     assert @buch.verfuegbar, 'Ein neues Buch sollte verfügbar sein'
#   end

#   def test_buch_ausleihen_aendert_verfuegbarkeit
#     @ausleiher.buch_ausleihen(@buch)
#     refute @buch.verfuegbar, 'Nach dem Ausleihen sollte das Buch nicht mehr verfügbar sein'
#   end

#   def test_buch_zurueckgeben_aendert_verfuegbarkeit
#     @ausleiher.buch_ausleihen(@buch)
#     @ausleiher.buch_zurueckgeben(@buch)
#     assert @buch.verfuegbar, 'Nach dem Zurückgeben sollte das Buch wieder verfügbar sein'
#   end

#   def test_erneutes_ausleihen_wirft_exception
#     @ausleiher.buch_ausleihen(@buch)
#     assert_raises(BuchBereitsAusgeliehenError) { @ausleiher.buch_ausleihen(@buch) }
#   end

#   def test_exception_enthaelt_buchtitel
#     @ausleiher.buch_ausleihen(@buch)
#     fehler = assert_raises(BuchBereitsAusgeliehenError) { @ausleiher.buch_ausleihen(@buch) }
#     assert_includes fehler.message, @buch.titel
#   end

#   def test_range_liefert_richtige_anzahl
#     buecher = [
#       Buch.new('Buch 1', 'Autor 1', '111'),
#       Buch.new('Buch 2', 'Autor 2', '222'),
#       Buch.new('Buch 3', 'Autor 3', '333'),
#       Buch.new('Buch 4', 'Autor 4', '444')
#     ]
#     auswahl = buecher[0..2] # Range: erste 3 Bücher
#     assert_equal 3, auswahl.length, 'Range 0..2 sollte 3 Bücher liefern'
#   end
# end
