# Zuerst erweitern wir die String-Klasse um die Methode 'titleize'.
# (Normalerweise würde man diese Erweiterung in eine eigene Datei auslagern und per require einbinden.)
class String
  # Wandelt einen String in Titel-Schreibweise um (jedes Wort wird großgeschrieben).
  def titleize
    gsub(/(\A|\s)\w/) { |letter| letter.upcase }
  end
end

# Nun laden wir die Minitest-Bibliothek, die die Testfunktionalität bereitstellt.
require 'minitest/autorun'

# Wir definieren einen Testfall, indem wir von Minitest::Test erben.
# In dieser Klasse können beliebig viele Testmethoden stehen, um die Tests logisch zu trennen.
class TestTitleize < Minitest::Test
  # Ein einfacher Testfall mit drei Assertions, die das Verhalten von 'titleize' prüfen.
  def test_basic
    assert_equal('This Is A Test', 'this is a test'.titleize)
    assert_equal('Another Test 1234', 'another test 1234'.titleize)
    assert_equal("We're Testing", "We're testing".titleize)
    assert_equal("Let's Make A Test Fail!", 'FooBar'.titleize)
  end
end
