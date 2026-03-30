class Pet
attr_accessor :name, :age, :gender, :color
end
# (the < operator, in this case, defines which class is inherited from)
class Cat < Pet
end
class Dog < Pet
end
class Snake < Pet
end

cat_instance = Cat.new
cat_instance.name = "Tigger"
cat_instance.age = 3
cat_instance.gender = "male"
cat_instance.color = "orange"
puts cat_instance.inspect


dog_instance = Dog.new
dog_instance.name = "Merlin"
dog_instance.age = 16
dog_instance.gender = "male"
dog_instance.color = "black/gray"
puts dog_instance.inspect

class Snake < Pet
attr_accessor :length
end

snake_instance = Snake.new
snake_instance.name = "Schlangi"
snake_instance.age = 5
snake_instance.gender = "female"
snake_instance.color = "rainbow"
snake_instance.length = 1.5
puts snake_instance.inspect


class Dog < Pet
  def bark
    puts "Wufff!"
  end
end
a_dog = Dog.new
a_dog.bark


class Cat < Pet
  def miau
    puts "Miauuu!"
  end
end

a_cat = Cat.new
a_cat.miau
