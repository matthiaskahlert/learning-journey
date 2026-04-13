# a) Klasse Circle mit Instanzmethode area und Klassenmethode count
class Circle
  @@count = 0 # legt eine klassenvariable an, speichert Anzahl der Kreisflächen

  attr_reader :radius # ermöglicht mir die nutzung von circle.radius

  def initialize(radius) # konstruktor
    @radius = radius
    @@count += 1 # erhöht den counter um 1 für jedes neue Kreisobjekt
  end

  def area # Instantmethode
    Math::PI * radius * radius # pi * r²
  end

  def self.count # Klassenmethode
    @@count # gibt die Anzahl der erzeugten Kreise zurück
  end

  def self.compare(circle1, circle2) # Klassenmethode zum Vergleich von zwei Kreisflächen
    circle1.area >= circle2.area ? circle1 : circle2 # ternary operator prüft auf größer oder =
  end
end

# b) Kreisobjekte erstellen und Methoden testen
circle1 = Circle.new(3)
circle2 = Circle.new(5)
circle3 = Circle.new(2)

puts "Fläche von Kreis 1: #{circle1.area.round(2)}"
puts "Fläche von Kreis 2: #{circle2.area.round(2)}"
puts "Fläche von Kreis 3: #{circle3.area.round(2)}"
puts "Anzahl erstellter Kreisobjekte: #{Circle.count}"

# c) Größeren Kreis über compare ermitteln
groesserer_kreis = Circle.compare(circle1, circle2)
puts "Der Kreis mit der größeren Fläche hat den Radius #{groesserer_kreis.radius}."
