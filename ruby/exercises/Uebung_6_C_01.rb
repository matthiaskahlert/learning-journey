# a) Erstelle die Klasse "GeometricShape" mit einer Instanzvariablen "@side_length". Definiere einen Konstruktor, der "@side_length" initialisiert.
class GeometricShape
  def initialize(side_length)
    @side_length = side_length
  end

  # b) Erstelle eine Methode "area" in der Klasse "GeometricShape", die den Flächeninhalt der Form berechnet.
  # Da diese Methode für jede spezifische Form unterschiedlich ist, sollte sie in der Basisklasse eine Ausnahme werfen.
  def area
    raise NotImplementedError, "Die Methode 'area' muss in einer abgeleiteten Klasse überschrieben werden."
  end
end

# c) Erstelle eine abgeleitete Klasse "Square", die von "GeometricShape" erbt.
# Überschreibe die Methode "area", um den Flächeninhalt eines Quadrats zu berechnen.
class Square < GeometricShape
  def area
    @side_length**2
  end
end

# d) Erstelle eine weitere abgeleitete Klasse "Triangle", die ebenfalls von "GeometricShape" erbt.
# Überschreibe die Methode "area", um den Flächeninhalt eines Dreiecks zu berechnen.
class Triangle < GeometricShape
  def area
    (@side_length**2) * Math.sqrt(3) / 4
  end
end

# e) Erstelle Instanzen von "Square" und "Triangle", gib ihren Flächeninhalt aus und vergleiche die Ergebnisse
square = Square.new(4)
triangle = Triangle.new(4)

puts "Flächeninhalt des Quadrats: #{square.area}"
puts "Flächeninhalt des Dreiecks: #{triangle.area}"
