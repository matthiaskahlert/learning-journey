# a) Erstelle ein Modul Pricing, das eine Methode calculate_price enthält. Diese Methode sollte zwei Parameter akzeptieren: base_price und tax_rate. Die Methode sollte den Preis nach Steuern berechnen und zurückgeben.

# b) Erstelle ein Modul Weight, das eine Methode calculate_weight enthält. Diese Methode sollte zwei Parameter akzeptieren: base_weight und packaging_weight. Die Methode sollte das Gesamtgewicht des Produkts berechnen und zurückgeben.

# c) Erstelle eine Klasse Product und inkludiere die Module Pricing und Weight. Füge der Klasse Product zusätzlich eine Methode details hinzu, die den Preis und das Gewicht des Produkts ausgibt.

# d) Erstelle eine Klasse Book und eine Klasse Furniture in einem Namespace Products, die beide von der Klasse Product erben. Überschreibe in beiden Klassen die Methoden calculate_price und calculate_weight mit spezifischen Berechnungen für Bücher bzw. Möbel.

require_relative 'pricing'
require_relative 'weight'

# Produktklasse mit Preis- und Gewichtsfunktionen
class Product
  include Pricing
  include Weight

  attr_accessor :name, :base_price, :tax_rate, :base_weight, :packaging_weight

  def initialize(name, base_price, tax_rate, base_weight, packaging_weight)
    @name = name
    @base_price = base_price
    @tax_rate = tax_rate
    @base_weight = base_weight
    @packaging_weight = packaging_weight
  end

  # Gibt Details zum Produkt aus
  def details
    price = calculate_price(@base_price, @tax_rate)
    weight = calculate_weight(@base_weight, @packaging_weight)
    "Produkt: #{@name}, Preis: #{format('%.2f', price)} EUR, Gewicht: #{format('%.2f', weight)} kg"
  end
end

# Namespace fuer spezifische Produkte
module Products
  # Buchklasse mit spezifischen Preis- und Gewichtsberechnungen
  class Book < Product
    attr_accessor :author

    def initialize(name, base_price, tax_rate, base_weight, packaging_weight, author)
      super(name, base_price, tax_rate, base_weight, packaging_weight)
      @author = author
    end

    def details
      "Buch: #{@name} von #{@author}, " + super
    end
  end

  # Moebelklasse mit spezifischen Preis- und Gewichtsberechnungen
  class Furniture < Product
    attr_accessor :material

    def initialize(name, base_price, tax_rate, base_weight, packaging_weight, material)
      super(name, base_price, tax_rate, base_weight, packaging_weight)
      @material = material
    end

    def details
      "Moebel: #{@name} aus #{@material}, " + super
    end
  end
end

# Beispielinstanzen und Ausgabe
book = Products::Book.new('Ruby Programming', 29.99, 7, 0.5, 0.2, 'John Doe')
furniture = Products::Furniture.new('Schreibtisch', 199.99, 19, 20, 5, 'Holz')

puts book.details
puts furniture.details
