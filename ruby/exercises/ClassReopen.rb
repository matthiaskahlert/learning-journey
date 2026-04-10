##
# Reopen von Integer fuer einfache Zeitberechnungen.
# @example
#   10.minutes
#   #=> 600
class Integer
  ##
  # Gibt den Wert als Sekunden zurueck.
  # @return [Integer] Sekunden.
  def seconds
    self
  end

  ##
  # Rechnet Minuten in Sekunden um.
  # @return [Integer] Sekundenwert.
  def minutes
    self * 60
  end

  ##
  # Rechnet Stunden in Sekunden um.
  # @return [Integer] Sekundenwert.
  def hours
    self * 60 * 60
  end

  ##
  # Rechnet Tage in Sekunden um.
  # @return [Integer] Sekundenwert.
  def days
    self * 60 * 60 * 24
  end
end
puts Time.now
puts Time.now + 10.minutes
puts Time.now + 16.hours
puts Time.now - 7.days
