require_relative 'a'
puts "Hello from b.rb"
require_relative 'a'
puts "Hello again from b.rb"
# das zweite require_relative 'a' führt nicht zu einer erneuten Ausführung von a.rb, da Ruby bereits weiß, dass es geladen wurde. Es wird also nur einmal "Hello from a.rb" ausgegeben, gefolgt von den beiden Ausgaben aus b.rb.
# 
