# Stell dir vor, du arbeitest an einer Software für ein Unternehmen, das verschiedene Arten von Produkten herstellt und verkauft. Jedes Produkt hat seine eigene Art, berechnet und beschrieben zu werden.

# a) Erstelle eine Klasse Product mit den grundlegenden Attributen wie name und price.

# b) Erstelle eine Methode description, die eine grundlegende Beschreibung des Produkts zurückgibt.

# c) Erstelle nun zwei weitere Klassen, Book und Electronics, die von der Product-Klasse erben. Beide Klassen sollten zusätzliche Attribute haben, die spezifisch für ihre Art von Produkt sind (z.B. könnte Book ein author-Attribut haben und Electronics könnte ein brand-Attribut haben).

# d) Überschreibe die description-Methode in beiden Klassen, um eine spezifischere Beschreibung zu geben, die die zusätzlichen Attribute berücksichtigt.

# e) Erstelle Instanzen von Book und Electronics und rufe die description-Methode auf, um zu überprüfen, ob die Polymorphie korrekt funktioniert.
#

##
# Basis-Klasse fuer Produkte mit Name und Preis.
# @example
#   p = Product.new('Notebook', 999.0)
#   p.description
class Product
  attr_accessor :name, :price

  ##
  # Initialisiert ein Produkt.
  # @param name [String] Name des Produkts.
  # @param price [Numeric] Preis des Produkts.
  # @return [void]
  def initialize(name, price)
    @name = name
    @price = price
  end

  ##
  # Liefert eine kurze Produktbeschreibung.
  # @return [String] Formatierter Beschreibungstext.
  def description
    "Produkt: #{@name}, Preis: #{format('%.2f', @price)} EUR"
  end
end

##
# Buch ist ein spezielles Produkt mit Autor.
# @example
#   Book.new('Der Hobbit', 14.99, 'J.R.R. Tolkien').description
class Book < Product
  attr_accessor :author

  ##
  # Initialisiert ein Buch.
  # @param name [String] Buchtitel.
  # @param price [Numeric] Preis.
  # @param author [String] Autorname.
  # @return [void]
  def initialize(name, price, author)
    super(name, price)
    @author = author
  end

  ##
  # Liefert eine spezifische Buchbeschreibung.
  # @return [String] Beschreibung mit Autor und Preis.
  def description
    "Buch: #{@name} von #{@author}, Preis: #{format('%.2f', @price)} EUR"
  end
end

##
# Elektronik ist ein Produkt mit Markeninformation.
# @example
#   Electronics.new('Kopfhoerer', 89.95, 'Sony').description
class Electronics < Product
  attr_accessor :brand

  ##
  # Initialisiert ein Elektronik-Produkt.
  # @param name [String] Produktname.
  # @param price [Numeric] Preis.
  # @param brand [String] Marke.
  # @return [void]
  def initialize(name, price, brand)
    super(name, price)
    @brand = brand
  end

  ##
  # Liefert eine spezifische Elektronik-Beschreibung.
  # @return [String] Beschreibung mit Marke und Preis.
  def description
    "Elektronik: #{@name} (Marke: #{@brand}), Preis: #{format('%.2f', @price)} EUR"
  end
end

book = Book.new('Der Hobbit', 14.99, 'J.R.R. Tolkien')
electronics = Electronics.new('Kopfhörer', 89.95, 'Sony')

products = [book, electronics]
products.each do |product|
  puts product.description
end
