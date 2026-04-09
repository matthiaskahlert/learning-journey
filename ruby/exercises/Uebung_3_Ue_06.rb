#Aufgabe Flow Control 
#Erstelle ein Ruby-Skript, das eine Variable bewertung definiert. Diese Variable sollte einen Wert zwischen 1 und 10 haben
# stelle sicher, dass bewertung nur zwischen 1 und 10 liegen kann.

bewertung = 7
 # b)
if bewertung >= 7
    puts "Guter Film!"
else
    puts "Schlechter Film!" 
end
# c)
if bewertung == 10
    puts "Fantastischer Film!"
elsif bewertung >= 7
    puts "Guter Film!"
elsif bewertung >= 1 && bewertung < 6
    puts "Nicht mein Geschmack!"
end


