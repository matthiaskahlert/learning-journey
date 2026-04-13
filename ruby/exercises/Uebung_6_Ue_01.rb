# Du arbeitest an einer Ruby-Anwendung, die eine Person-Klasse verwendet.
# Die Person-Klasse hat zwei private Methoden:
# set_first_name(name) und set_last_name(name), die verwendet werden,
# um den Vornamen und den Nachnamen einer Person zu setzen.

# a) Erstelle eine neue Klasse Student, die von der Person-Klasse erbt.
# In dieser neuen Klasse, überschreibe die set_first_name(name) Methode,
# so dass sie zusätzlich überprüft, ob der Name mindestens 2 Zeichen lang ist.
# Wenn dies nicht der Fall ist, sollte die Methode eine Ausnahme auslösen.

# b) Erstelle eine Instanz der Student-Klasse und versuche,
# einen Vornamen mit weniger als 2 Zeichen zu setzen. Was passiert?

# c) Wie würdest du die set_last_name(name) Methode überschreiben,
# um eine ähnliche Überprüfung durchzuführen?

class Person
  private

  def set_first_name(name)
    @first_name = name
  end

  def set_last_name(name)
    @last_name = name
  end
end

class Student < Person
  private

  def set_first_name(name)
    raise 'Vorname muss mindestens zwei Zeichen lang sein.' if name.length < 2

    super(name)
  end

  def set_last_name(name)
    raise 'Nachname muss mindestens zwei Zeichen lang sein.' if name.length < 2

    super(name)
  end
end

# Test cases
student = Student.new
begin
  student.send(:set_first_name, 'A') # Dies sollte eine exception auslösen
rescue StandardError => e
  puts "Fehler: #{e.message}"
end

begin
  student.send(:set_last_name, 'B') # Dies sollte eine exception auslösen
rescue StandardError => e
  puts "Fehler: #{e.message}"
end
