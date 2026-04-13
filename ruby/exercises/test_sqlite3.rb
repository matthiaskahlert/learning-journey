# Test: sqlite3 Gem funktioniert?
require 'sqlite3'

# Datenbank erstellen/oeffnen
$db = SQLite3::Database.new('testdb.db')
$db.results_as_hash = true

# Einfache Tabelle anlegen
$db.execute <<-SQL
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
  );
SQL

# Ein paar Daten einfügen
$db.execute('INSERT INTO users (name, age) VALUES (?, ?)', ['Fred Bloggs', 45])
$db.execute('INSERT INTO users (name, age) VALUES (?, ?)', ['Laura Smith', 23])

# Daten abrufen und ausgeben
results = $db.execute('SELECT * FROM users')
results.each do |row|
  puts "#{row['name']} ist #{row['age']} Jahre alt"
end

puts "\n✓ SQLite3 funktioniert erfolgreich!"

# Aufruäumen
$db.close
