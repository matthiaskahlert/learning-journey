# TDD-Beispiel: titleize
# Ziel: Strings in Titel-Schreibweise umwandeln.

class String
  def titleize
    # gsub(/\b\w/) { |letter| letter.upcase } # tdd_titleize_example.rb:14:in '<main>': Fail 3 (RuntimeError)
    gsub(/(\A|\s)\w/) { |letter| letter.upcase }
  end
end

# Assertions (Testfall-Set)
raise 'Fail 1' unless 'this is a test'.titleize == 'This Is A Test'
raise 'Fail 2' unless 'another test 1234'.titleize == 'Another Test 1234'
raise 'Fail 3' unless "We're testing titleize".titleize == "We're Testing Titleize"

puts 'Alle TDD-Tests fuer titleize sind erfolgreich.'
