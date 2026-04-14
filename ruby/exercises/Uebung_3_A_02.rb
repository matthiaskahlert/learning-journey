# a) Definiere eine Variable namens "students" und weise ihr ein Array von Hashes zu. Jeder Hash sollte die Informationen eines Studenten enthalten: Name, Alter und Notendurchschnitt.

students = [
  { name: 'Anna',  age: 22, grade: 1.7 },
  { name: 'Ben',   age: 17, grade: 2.3 },
  { name: 'Clara', age: 19, grade: 3.0 },
  { name: 'David', age: 21, grade: 1.3 },
  { name: 'Eva',   age: 16, grade: 2.7 }
]

# b) Erstelle eine Funktion, die die Durchschnittsnote aller Studenten berechnet und ausgibt.

def average_grade(students)
  avg = students.sum { |s| s[:grade] } / students.size.to_f
  puts "Durchschnittsnote: #{avg.round(2)}"
end

average_grade(students)

# c) Erstelle eine Funktion, die einen Bereich von Zahlen akzeptiert und eine neue Liste von Studenten erstellt, die nur die Studenten enthält, deren Notendurchschnitt innerhalb dieses Bereichs liegt.

def students_in_grade_range(students, range)
  students.select { |s| range.include?(s[:grade]) }
end

puts "\nStudenten mit Note zwischen 1.0 und 2.0:"
students_in_grade_range(students, 1.0..2.0).each { |s| puts "  #{s[:name]}: #{s[:grade]}" }

# d) Erstelle eine Funktion, die eine Bedingung akzeptiert (zum Beispiel, ob das Alter eines Studenten größer als 18 ist) und die Studentenliste filtert, um nur die Studenten anzuzeigen, die diese Bedingung erfüllen.

def filter_students(students, &condition)
  students.select(&condition)
end

puts "\nStudenten älter als 18:"
filter_students(students) { |s| s[:age] > 18 }.each { |s| puts "  #{s[:name]}, #{s[:age]} Jahre" }

# e) Erstelle eine Funktion, die eine Nummer akzeptiert und prüft, ob diese Nummer in den Altersangaben der Studenten vorhanden ist. Wenn ja, sollte die Funktion "true" zurückgeben, andernfalls "false".

def age_exists?(students, age)
  students.any? { |s| s[:age] == age }
end

puts "\nGibt es einen Studenten mit Alter 19? #{age_exists?(students, 19)}"
puts "Gibt es einen Studenten mit Alter 30? #{age_exists?(students, 30)}"
