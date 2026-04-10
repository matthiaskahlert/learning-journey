# Zeigt alle Verzeichnisse, die Ruby durchsucht, wenn man 'require' nutzt
puts "=" * 50
puts "Ruby Load Path: Alle Suchverzeichnisse"
puts "=" * 50

$:.each { |d| puts d }

puts "=" * 50
puts "Insgesamt #{$:.length} Verzeichnisse"
