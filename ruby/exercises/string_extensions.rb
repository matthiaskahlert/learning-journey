##
# Kleine Erweiterung fuer Strings: alle Vokale auslesen.
# @example
#   'This is a test'.vowels
#   #=> ["i", "i", "a", "e"]
class String
  ##
  # Gibt alle Vokale als Array zurueck (gross/klein egal).
  # @return [Array<String>] Alle gefundenen Vokale in Reihenfolge.
  # @example
  #   'Ruby'.vowels
  #   #=> ["u"]
  def vowels
    scan(/[aeiou]/i)
  end
end
