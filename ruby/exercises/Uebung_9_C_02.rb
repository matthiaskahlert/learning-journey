# Du arbeitest als Softwareentwickler in einer Firma, die eine große Menge an Daten verarbeitet. Du erhältst die Aufgabe, ein Ruby-Programm zu schreiben, das Daten von einer Datei liest und verarbeitet.

# a) Entwickle ein Ruby-Skript, das eine Datei mit dem Namen "data.txt" öffnet und liest. Jede Zeile in der Datei repräsentiert einen Datensatz, der aus drei Teilen besteht, die durch Kommas getrennt sind. Zum Beispiel: "Teil1,Teil2,Teil3".

# b) Wende eine Ausnahmebehandlung an, um sicherzustellen, dass dein Programm ordnungsgemäß funktioniert, auch wenn die Datei nicht existiert oder andere Fehler auftreten. Wenn ein Fehler auftritt, sollte dein Programm eine benutzerdefinierte Fehlermeldung ausgeben, die den Benutzer über das Problem informiert.

# c) Modifiziere dein Programm, um die Daten zu analysieren und zu quantifizieren. Zum Beispiel, zähle die Anzahl der Datensätze, die einen bestimmten Wert in einem der Teile haben.

# a) + b) Datei lesen mit Ausnahmebehandlung
def lese_datei(dateiname)
  datensaetze = []
  File.foreach(dateiname) do |zeile|
    teile = zeile.chomp.split(',') # Zeile an Komma trennen
    datensaetze << teile
  end
  datensaetze
rescue Errno::ENOENT
  puts "Fehler: Die Datei '#{dateiname}' wurde nicht gefunden."
  []
rescue StandardError => e
  puts "Unbekannter Fehler beim Lesen der Datei: #{e.message}"
  []
end

# c) Datensätze analysieren – zählt wie viele Einträge einen bestimmten Wert in einem Teil haben
def zaehle_datensaetze(datensaetze, suchwert, teil_index)
  datensaetze.count { |teile| teile[teil_index]&.strip == suchwert }
end

# Hauptprogramm
dateiname = File.join(__dir__, 'data.txt') # Pfad relativ zur aktuellen Datei
datensaetze = lese_datei(dateiname)

unless datensaetze.empty?
  puts "Datei erfolgreich gelesen. #{datensaetze.length} Datensätze gefunden.\n\n"

  # Alle Datensätze ausgeben
  datensaetze.each_with_index do |teile, index|
    puts "Datensatz #{index + 1}: Teil1=#{teile[0]}, Teil2=#{teile[1]}, Teil3=#{teile[2]}"
  end

  # c) Analyse: Wie viele Datensätze haben "aktiv" in Teil3?
  suchwert = 'aktiv'
  anzahl = zaehle_datensaetze(datensaetze, suchwert, 2) # Index 2 = Teil3
  puts "\nAnzahl der Datensätze mit '#{suchwert}' in Teil3: #{anzahl}"
end
