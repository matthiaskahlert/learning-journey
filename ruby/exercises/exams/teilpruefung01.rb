# a) Ein beliebiger Text mit mehr als 1000 Zeichen wurde in der Variable text gespeichert.
text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' * 25).strip
puts "Textlänge: Der Text hat #{text.length} Zeichen"

# b) Prüfung mit if
puts 'Der Text ist zu lang' if text.length > 1000

# c) Prüfung mit unless
# puts 'Der Text ist nicht zu lang' unless text.length > 1000
# Testausgaben
# text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' * 5).strip # Test auf unter 1000 Zeichen
puts 'Der Text ist nicht zu lang' unless text.length > 1000

# d) Prüfung mit ternary operator
# Testausgaben
# text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' * 5).strip # Test auf unter 1000 Zeichen
puts(text.length > 1000 ? 'Der Text ist zu lang' : 'Der Text ist nicht zu lang')

# e) Prüfung mit elsif
# Testausgaben
# text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' * 5).strip # Test auf unter 1000 Zeichen
# text = ('Loremipsum' * 50).strip # Test auf genau 500 Zeichen
if text.length > 1000
  puts 'Der Text ist zu lang'
elsif text.length == 500
  puts 'Der Text hat genau 500 Zeichen'
else
  puts 'Der Text ist nicht zu lang'
end
