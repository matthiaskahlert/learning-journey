zahl1 = 10
zahl2 = 20
zahl3 = 30
puts "Die zahlen lauten: #{zahl1}, #{zahl2} und #{zahl3}."
puts "Die Summe der Zahlen ist #{zahl1 + zahl2 + zahl3}."
puts "Die Differenz der Zahlen ist #{zahl1 - zahl2 - zahl3}."
puts "Das Produkt der Zahlen ist #{zahl1 * zahl2 * zahl3}."
puts " Der Quotient der Zahlen ist #{zahl1.to_f / zahl2 / zahl3}."

1.upto(10) { |i| puts i*zahl1 }
