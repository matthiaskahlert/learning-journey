# a) Erstelle eine Basisklasse Animal mit einer Instanzvariablen name 
# und einer Methode initialize, die den Namen des Tieres als Parameter akzeptiert 
# und diesen Namen der Instanzvariablen zuweist.
class Animal
  def initialize(name)
    @name = name
  end

  # d) Demonstriere die Verwendung von Encapsulation, 
  # indem die Instanzvariable @name geschützt wird.
  private

  attr_reader :name
end

# b) Erstelle zwei Unterklassen Dog und Cat, die von der Animal-Klasse erben.
class Dog < Animal
  def sound
    'Wuff!'
  end
end

class Cat < Animal
  def sound
    'Miau!'
  end
end

# c) Erstelle eine Array mit verschiedenen Tierobjekten (Hunde und Katzen) 
# und iteriere über diese Array, um das Geräusch jedes Tieres auszugeben.
animals = [
  Dog.new('Paul-Alfred'),
  Cat.new('Morle'),
  Dog.new('Berry'),
  Cat.new('Tessy')
]

animals.each do |animal|
  puts animal.sound
end
