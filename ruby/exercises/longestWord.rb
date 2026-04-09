my_array = %w[this is a test of the longest word check] # Ein Array mit mehreren Wörtern

longest_word = '' # Variable für das bisher längste gefundene Wort

# Gehe jedes Wort im Array durch
my_array.each do |word|
  # Wenn das aktuelle Wort länger ist als das bisher gespeicherte längste Wort, ersetze longest_word
  longest_word = word if longest_word.length < word.length
end

puts longest_word # Gib das längste Wort aus

my_array = %w[10 56 92 3 49 588 18]
highest_number = 0
my_array.each do |number|
  number = number.to_i
  highest_number = number if number > highest_number
end
puts highest_number
