 # Ursprünglicher String (wird gleich überschrieben)
s = "Ich lerne Ruby und es macht Spaß!"

# Name definieren
name = "Matthias"

# String mit Name und Interpolation neu zuweisen
s = "Ich, #{name}, lerne Ruby und versuche daran Spaß zu haben."

# Gib den String aus
p s

# Gib den String in Großbuchstaben aus
p s.upcase

# Prüfe, ob "Ruby" im String enthalten ist
p s.include?("Ruby")

# Zähle die Wörter im String und gib das Ergebnis aus
p "Die Anzahl der Wörter im string '#{s}' beträgt '#{s.split.size}'."
