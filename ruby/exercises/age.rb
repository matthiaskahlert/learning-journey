age = 24
puts "You're NOT a teenager, you are #{age} years old." unless age > 12 && age < 20

age = 10
puts "You're too young to use this system, because #{age} is less then 18." if age < 18

age=45
puts "You are a grown up because #{age} is between 20 and 64." if age.between?(20, 64)

