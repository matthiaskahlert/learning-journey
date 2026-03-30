class Person
  attr_accessor :name, :age, :gender
end

person_instance = Person.new

person_instance.name = "Matthias"
person_instance.age = 45
person_instance.gender = "male"
puts person_instance.inspect

=begin  
accessor bedeutet sinngemäß: „Mach diese Attribute frei zugänglich, 
sodass sie jederzeit gesetzt und verändert werden können." 
Das heißt: Wenn ich mit einem Person-Objekt arbeite, kann ich den Namen, 
das Alter und das Geschlecht dieser Person jederzeit lesen und ändern.
=end
