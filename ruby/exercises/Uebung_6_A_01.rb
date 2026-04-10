# Stell dir vor, du arbeitest an einer Software für ein Unternehmen, das verschiedene Arten von Produkten herstellt und verkauft. Jedes Produkt hat seine eigene Art, berechnet und beschrieben zu werden.

# a) Erstelle eine Klasse Product mit den grundlegenden Attributen wie name und price.

# b) Erstelle eine Methode description, die eine grundlegende Beschreibung des Produkts zurückgibt.

# c) Erstelle nun zwei weitere Klassen, Book und Electronics, die von der Product-Klasse erben. Beide Klassen sollten zusätzliche Attribute haben, die spezifisch für ihre Art von Produkt sind (z.B. könnte Book ein author-Attribut haben und Electronics könnte ein brand-Attribut haben).

# d) Überschreibe die description-Methode in beiden Klassen, um eine spezifischere Beschreibung zu geben, die die zusätzlichen Attribute berücksichtigt.

# e) Erstelle Instanzen von Book und Electronics und rufe die description-Methode auf, um zu überprüfen, ob die Polymorphie korrekt funktioniert.
#

class Product
  attr_accessor :name, :price

  def initialize(name, price)
    @name = name
    @price = price
  end

  def description
    "Produkt: #{@name}, Preis: #{format('%.2f', @price)} EUR"
  end
end

class Book < Product
  attr_accessor :author

  def initialize(name, price, author)
    super(name, price)
    @author = author
  end

  def description
    "Buch: #{@name} von #{@author}, Preis: #{format('%.2f', @price)} EUR"
  end
end

class Electronics < Product
  attr_accessor :brand

  def initialize(name, price, brand)
    super(name, price)
    @brand = brand
  end

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
