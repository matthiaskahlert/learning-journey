# a) Was ist ein Hash und wie wird er erstellt??
# b) Wie greift man auf die Werte in einem Hash zu?
# c) Wie kann man die Schlüssel und Werte in einem Hash anzeigen?
# d) Wie kann man Elemente aus einem Hash löschen?
# e) Wie kann man Elemente aus einem Hash basierend auf bestimmten Bedingungen löschen?
# f) Wie kann man Hashes innerhalb von Hashes erstellen und darauf zugreifen?

# a)
# Ein Hash ist eine Sammlung von Schlüssel-Wert-Paaren (ähnlich wie ein Dictionary in anderen Sprachen).
# Jeder Schlüssel (key) zeigt auf einen Wert (value).

# Beispiel:
person = {
  name: 'Max',
  age: 25,
  city: 'Berlin'
}

# name, age, city = Schlüssel
# "Max", 25, "Berlin" = Werte

# Alternative Schreibweise:

person = {}
person[:name] = 'Max'

# b)
# Zugriff auf Werte in einem Hash erfolgt über die Schlüssel.
# Du greifst über den Schlüssel auf den Wert zu:

puts person[:name]   # => Max
puts person[:age]    # => 25

# Wichtig: Schlüssel müssen exakt stimmen (Symbole vs. Strings!)
person['name'] # => nil (wenn Schlüssel :name ist)

# c)
# Alle Schlüssel anzeigen:
puts person.keys # => [:name, :age, :city]

puts person.values # => ["Max", 25, "Berlin"]

# Alle Schlüssel-Wert-Paare anzeigen:
# Alles anzeigen:
puts "Gesamter Hash als Ruby string: #{person.inspect}" # => {:name=>"Max", :age=>25, :city=>"Berlin"}

# oder folgender Ausdruck gibt jeses Paar einzeln aus:
person.each do |key, value|
  puts "#{key}: #{value}"
end

# d)
# Elemente aus einem Hash löschen:
# delete-Methode:
person.delete(:age) # => 25 (entfernt das Schlüssel-Wert-Paar
puts person.inspect # => {:name=>"Max", :city=>"Berlin"}

# mehrere löschen

person.delete(:name)
person.delete(:city)

# e) Löschen mit Bedingungen
# Beispiel: Lösche alle Werte < 30
person = {
  max: 25,
  anna: 32,
  tom: 19
}

person.delete_if do |key, value|
  value < 30
end
puts person.inspect # => {:anna=>32}

# f) Hashes in Hashes (verschachtelt)
# Du kannst Hashes ineinander verschachteln:

users = {
  user1: {
    name: 'Max',
    age: 25
  },
  user2: {
    name: 'Anna',
    age: 30
  }
}
# Zugriff auf verschachtelte Werte:
puts users[:user1][:name]  # => Max
puts users[:user2][:age]   # => 30

# Iteration durch verschachtelte Werte:

users.each do |user, data|
  puts "User: #{user}"
  data.each do |key, value|
    puts "  #{key}: #{value}"
  end
end
# 1. users.each geht jeden Eintrag im äußeren Hash durch.
#   user ist dann z.B. :user1, data ist { name: 'Max', age: 25 }

# 2. puts "User: #{user}" gibt z.B. User: user1 aus.

# 3. data.each geht jetzt durch den inneren Hash (also durch name und age).
#   key ist z.B. :name, value ist "Max"
#   puts " #{key}: #{value}" gibt z.B. " name: Max" aus.
#   