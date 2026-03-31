s = "Ich lerne Ruby und es macht Spaß!"
name = "Matthias"
s = "Ich, #{name}, lerne Ruby und versuche daran Spaß zu haben."
p s
p s.upcase

p s.include?("Ruby")


p "Die Anzahl der Wörter im string '#{s}' beträgt '#{s.split.size}'."
