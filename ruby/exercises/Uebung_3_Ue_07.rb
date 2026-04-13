# a) Definiere eine Variable start_date, die ein Time-Objekt repräsentiert, das auf den 1. Januar 2022 um 00:00:00 Uhr eingestellt ist.
start_date = Time.new(2022, 1, 1, 0, 0, 0)

# b) Definiere eine Variable end_date, die ein Time-Objekt repräsentiert, das auf den 31. Dezember 2022 um 23:59:59 Uhr eingestellt ist.
end_date = Time.new(2022, 12, 31, 23, 59, 59)

# c) Erstelle einen Bereich, der alle Sekunden von start_date bis end_date umfasst.
seconds_range = (start_date.to_i..end_date.to_i)

# d) Durchlaufe diesen Bereich und gib für jede Sekunde, die auf den Anfang einer Stunde fällt, folgendes aus:
# "Die aktuelle Stunde ist: X" (wobei X die aktuelle Stunde ist).
seconds_range.each do |second|
  time = Time.at(second)
  puts "Die aktuelle Stunde ist: #{time.hour}" if time.min == 0 && time.sec == 0
end

# e) Definiere ein Symbol für jeden Wochentag (Montag bis Sonntag).
weekdays = {
  monday: :Montag,
  tuesday: :Dienstag,
  wednesday: :Mittwoch,
  thursday: :Donnerstag,
  friday: :Freitag,
  saturday: :Samstag,
  sunday: :Sonntag
}

# f) Durchlaufe den Bereich erneut und gib für jeden Tag, der auf einen Montag fällt, folgendes aus:
# "Heute ist: X" (wobei X das Symbol für Montag ist).
seconds_range.each do |second|
  time = Time.at(second)
  puts "Heute ist: #{weekdays[:monday]}" if time.monday? && time.hour == 0 && time.min == 0 && time.sec == 0
end
