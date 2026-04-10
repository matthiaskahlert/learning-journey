##
# Basis-Klasse fuer Haustiere mit gemeinsamen Attributen.
# @example
#   pet = Pet.new
#   pet.name = 'Tigger'
class Pet
  attr_accessor :name, :age, :gender, :color
end

# (the < operator, in this case, defines which class is inherited from)
##
# Katzenklasse, erbt gemeinsame Eigenschaften von Pet.
class Cat < Pet
end

##
# Hundeklasse, erbt gemeinsame Eigenschaften von Pet.
class Dog < Pet
end

##
# Schlangenklasse, erbt gemeinsame Eigenschaften von Pet.
class Snake < Pet
end

cat_instance = Cat.new
cat_instance.name = 'Tigger'
cat_instance.age = 3
cat_instance.gender = 'male'
cat_instance.color = 'orange'
puts cat_instance.inspect

dog_instance = Dog.new
dog_instance.name = 'Merlin'
dog_instance.age = 16
dog_instance.gender = 'male'
dog_instance.color = 'black/gray'
puts dog_instance.inspect

class Snake < Pet
  attr_accessor :length
end

snake_instance = Snake.new
snake_instance.name = 'Schlangi'
snake_instance.age = 5
snake_instance.gender = 'female'
snake_instance.color = 'rainbow'
snake_instance.length = 1.5
puts snake_instance.inspect

class Dog < Pet
  ##
  # Gibt den Hunde-Laut aus.
  # @return [void]
  # @example
  #   Dog.new.bark
  def bark
    puts 'Wufff!'
  end
end
a_dog = Dog.new
a_dog.bark

class Cat < Pet
  ##
  # Gibt den Katzen-Laut aus.
  # @return [void]
  # @example
  #   Cat.new.miau
  def miau
    puts 'Miauuu!'
  end
end

a_cat = Cat.new
a_cat.miau
