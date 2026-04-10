# load 'ruby\exercises\string_extensions.rb'
# # Man nutzt loadum externe source code files in das programmzu laden
require_relative 'string_extensions'
# require_relative 'string_extensions' sucht relativ zur aktuellen Datei, nicht zum Working Directory. Das ist der Standard-Weg in Ruby

puts 'This is a test'.vowels.join('-')
