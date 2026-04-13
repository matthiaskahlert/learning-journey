# Du arbeitest für ein Unternehmen, das eine Software für ein Tierheim entwickelt. Das Tierheim hat verschiedene Arten von Tieren wie Hunde, Katzen, Vögel und Reptilien. Jedes Tier hat seine eigenen Eigenschaften und Verhaltensweisen. Deine Aufgabe ist es, eine Ruby-Anwendung zu erstellen, die diese Tiere und ihre Verhaltensweisen darstellt.

# a) Erstelle eine Basisklasse Animal, die Attribute wie name, age und species hat. Diese Klasse sollte eine Methode initialize haben, die diese Attribute initialisiert.

# b) Erstelle spezielle Klassen für Dog, Cat, Bird und Reptile, die von der Animal-Klasse erben. Jede dieser Klassen sollte eine Methode talk haben, die eine artenspezifische Botschaft zurückgibt (z.B. "Woof!" für Dog, "Meow!" für Cat, etc.).

# c) Erstelle eine Klasse Shelter, die eine Liste von Tieren enthält. Diese Klasse sollte Methoden haben, um Tiere hinzuzufügen und zu entfernen, und eine Methode make_all_animals_talk, die die talk-Methode für jedes Tier in der Liste aufruft.

# d) Demonstriere die Verwendung deiner Klassen, indem du einige Tiere erstellst, sie zum Tierheim hinzufügst und alle Tiere im Tierheim sprechen lässt.

class Animal
  attr_accessor :name, :age, :species

  def initialize(name, age, species)
    @name = name
    @age = age
    @species = species
  end
end

class Dog < Animal
  def talk
    'Wuff'
  end
end

class Cat < Animal
  def talk
    'Miau'
  end
end

class Bird < Animal
  def talk
    'Zwitscher!'
  end
end

class Reptile < Animal
  def talk
    'Zisch!'
  end
end

class Shelter
  def initialize
    @animals = []
  end

  def add_animal(animal)
    @animals << animal
  end

  def remove_animal(animal)
    @animals.delete(animal)
  end

  def make_all_animals_talk
    @animals.each do |animal|
      puts "#{animal.name} (#{animal.species}): #{animal.talk}"
    end
  end
end

# Demonstration
shelter = Shelter.new

dog = Dog.new('Paul-Alfred', 3, 'Dog')
cat = Cat.new('Morle', 2, 'Cat')
bird = Bird.new('Tweety', 1, 'Bird')
reptile = Reptile.new('Kroki', 4, 'Reptile')

shelter.add_animal(dog)
shelter.add_animal(cat)
shelter.add_animal(bird)
shelter.add_animal(reptile)

shelter.make_all_animals_talk
