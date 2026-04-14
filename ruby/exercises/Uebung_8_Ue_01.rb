# a) Erstelle ein Ruby-Skript, das 1000 zufällige Zahlen generiert.
# Wenn die Zahl 123 generiert wird, soll das Skript eine Ausnahme auslösen.

# b) Führe das Skript aus und beobachte, was passiert, wenn die Ausnahme ausgelöst wird.

# c) Verwende den Ruby-Debugger, um das Skript zu debuggen.
# Setze einen Breakpoint an der Stelle, an der die Ausnahme ausgelöst wird.

# d) Wenn der Breakpoint erreicht ist, untersuche die Variablen und führe Methoden aus,
# um zu verstehen, was passiert.

# e) Behandle die Ausnahme, indem du einen rescue-Block hinzufügst,
# um die Ausnahme zu fangen und eine Nachricht auszugeben

# Hinweis: catch/throw ist in Ruby kein Exception-Handling, sondern ein Control-Flow-Mechanismus.
# Für Ausnahmen (Exceptions) verwendet man raise und rescue.

# a) + b) + e): raise löst die Ausnahme aus, rescue fängt sie
begin
  1000.times do |i|
    x = rand(1000)
    # c) Hier wäre der Breakpoint im Debugger zu setzen
    # d) Im Debugger: "x" und "i" untersuchen, z.B. mit "p x" oder "info locals"
    raise "Die Zahl 123 wurde bei Iteration #{i + 1} generiert!" if x == 123
  end
  puts '1000 Zahlen generiert, ohne 123 zu erzeugen!'
rescue RuntimeError => e
  # e) Ausnahme wird gefangen und Nachricht ausgegeben
  puts "Ausnahme gefangen: #{e.message}"
end
