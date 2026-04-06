cities = {
  Berlin: 3_769_495,
  Hamburg: 1_845_229,
  München: 1_471_508,
  Köln: 1_087_863,
  Frankfurt: 753_056
}

puts "a) Einwohnerzahl München: #{cities[:München]}"

# b) Füge Stuttgart hinzu
cities[:Stuttgart] = 634_830
puts "b) Stuttgart hinzugefügt: #{cities[:Stuttgart]}"

# c) Entferne Frankfurt
cities.delete(:Frankfurt)
puts "c) Frankfurt entfernt. Aktuelle Städte: #{cities.keys}"

# d) Alle Städte auflisten (keys)
puts "d) Alle Städte: #{cities.keys}"

# e) Alle Bevölkerungszahlen auflisten (values)
puts "e) Alle Bevölkerungszahlen: #{cities.values}"

# f)
# cities.keys gibt ein Array aller Schlüssel (Städtenamen) im Hash zurück.
# cities.values gibt ein Array aller Werte (Bevölkerungszahlen) im Hash zurück.
