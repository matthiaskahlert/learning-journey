# a) Erstelle ein Array in Ruby, das die Zahlen von 1 bis 10 enthält.
# b) Füge dem Array die Zahlen 11 bis 20 hinzu.
# c) Entferne die ersten 5 Elemente aus dem Array.
# d) Überprüfe, ob die Zahl 15 in deinem Array vorhanden ist.
# e) Sortiere das Array in absteigender Reihenfolge.
# f) Berechne die Summe aller Zahlen in deinem Array.

array = (1..10).to_a # es ginge auch array = [1,2,3,4,5,6,7,8,9,10]
p array
array += (11..20).to_a
p array
array.shift(5)
p array
p array.include?(15)
array.sort!.reverse!
p array
puts array.sum
