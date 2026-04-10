# __dir__        = Das Verzeichnis, in dem DIESE DATEI (b_load.rb) liegt
# File.join()    = Verbindet Pfade sicher (funktioniert auf Windows, Mac, Linux)
# Zusammen: Lade die Datei 'a.rb' aus dem gleichen Verzeichnis wie b_load.rb

load File.join(__dir__, 'a.rb')
puts 'Hello from b.rb'

# Lädt a.rb nochmal - load führt den Code jedes Mal erneut aus (nicht gecacht)
load File.join(__dir__, 'a.rb')
puts 'Hello again from b.rb'
